#include <Motoron.h>

MotoronI2C mc;

//Microcontroller power
const uint16_t referenceMv = 5000;

//Specification of what motor type we are using
const MotoronCurrentSenseType type = MotoronCurrentSenseType::Motoron18v18;

// Minimum allowed VIN voltage
const uint16_t minVinVoltageMv = 6500;

const uint16_t units = mc.currentSenseUnitsMilliamps(type, referenceMv);

void calibrateCurrent() {
  mc.setSpeed(1, 0);
  mc.setSpeed(2, 0);

  // Testing samples
  const uint8_t desiredSampleCount = 64;
  uint8_t sampleCount = 0;
  uint16_t total[2] = {0, 0};

  // Monitoring the time since we started the test
  uint16_t lastTimeConditionsNotMet = millis();

  while(1) {
    // Create mask for checking the desired state of the motor in the specific moment
    const uint16_t statusMask = (1 << MOTORON_STATUS_FLAG_MOTOR_FAULTING) |
      (1 << MOTORON_STATUS_FLAG_NO_POWER) |
      (1 << MOTORON_STATUS_FLAG_MOTOR_OUTPUT_ENABLED) |
      (1 << MOTORON_STATUS_FLAG_MOTOR_DRIVING);
    const uint16_t statusDesired = (1 << MOTORON_STATUS_FLAG_MOTOR_OUTPUT_ENABLED);

    // If the desired status is not met or the voltage is too low, we monitor the abnormality
    if((mc.getStatusFlags() & statusMask) != statusDesired || mc.getVinVoltageMv(referenceMv) < minVinVoltageMv) {
      lastTimeConditionsNotMet = millis();
      sampleCount = 0;
      total[0] = total[1] = 0;
    }

    // Collecting sample data
    if(((uint16_t) millis() - lastTimeConditionsNotMet) > 20) {
      total[0] += mc.getCurrentSenseRaw(1);
      total[1] += mc.getCurrentSenseRaw(2);

      if (++sampleCount == desiredSampleCount) { break; }
    }
  }

  // Averaging each sample and also rounding if possible in order to get an accurate offset
  mc.setCurrentSenseOffset(1, (total[0] + desiredSampleCount / 2) / desiredSampleCount);
  mc.setCurrentSenseOffset(2, (total[1] + desiredSampleCount / 2) / desiredSampleCount);
  // Make the data more readable
  mc.setCurrentSenseMinimumDivisor(1, 100);
  mc.setCurrentSenseMinimumDivisor(2, 100);

  // Use flash memory instead of SRAM for the serial print of the offset
  Serial.print(F("Current sense offsets: "));
  Serial.print(mc.getCurrentSenseOffset(1));
  Serial.print(' ');
  Serial.print(mc.getCurrentSenseOffset(2));
}

// Current readability
void printCurrent(uint16_t processed)
{
  Serial.print(processed);
  Serial.print(F(" = "));
  uint32_t ma = (uint32_t)processed * units;
  Serial.print(ma);
  Serial.println(F(" mA"));
}

void setup() {
  Serial.begin(9600);

  Wire.begin();

  mc.reinitialize();
  mc.clearResetFlag();

  // Configure motor 1
  mc.setMaxAcceleration(1, 200);
  mc.setMaxDeceleration(1, 200);

  // Configure motor 2
  mc.setMaxAcceleration(2, 200);
  mc.setMaxDeceleration(2, 200);

  calibrateCurrent();

  // Set current limit based on the calculated offset
  mc.setCurrentLimit(1, mc.calculateCurrentLimit(10000,
    type, referenceMv, mc.getCurrentSenseOffset(1)));
  mc.setCurrentLimit(2, mc.calculateCurrentLimit(10000,
    type, referenceMv, mc.getCurrentSenseOffset(2)));
}

void loop()
{
  mc.setSpeed(1, 200);
  delay(1000);
  Serial.print(F("Motor 1 current: "));
  printCurrent(mc.getCurrentSenseProcessed(1));
  mc.setSpeed(1, 0);
  delay(1000);

  mc.setSpeed(2, 200);
  delay(1000);
  Serial.print(F("Motor 2 current: "));
  printCurrent(mc.getCurrentSenseProcessed(2));
  mc.setSpeed(2, 0);
  delay(1000);
}
