#include <Motoron.h>

MotoronI2C mc;

const auto vinType = MotoronVinSenseType::MotoronHp;
const uint16_t referenceMv = 5000;
const uint16_t minVinVoltageMv = 6500;
const uint8_t forward = 1;
const uint8_t backward = 2;
const uint8_t left = 3;
const uint8_t right = 4;

const uint16_t errorMask = 
  (1 << MOTORON_STATUS_FLAG_PROTOCOL_ERROR) |
  (1 << MOTORON_STATUS_FLAG_CRC_ERROR) |
  (1 << MOTORON_STATUS_FLAG_COMMAND_TIMEOUT_LATCHED) |
  (1 << MOTORON_STATUS_FLAG_MOTOR_FAULT_LATCHED) |
  (1 << MOTORON_STATUS_FLAG_NO_POWER_LATCHED) |
  (1 << MOTORON_STATUS_FLAG_RESET) |
  (1 << MOTORON_STATUS_FLAG_COMMAND_TIMEOUT) |
  (1 << MOTORON_STATUS_FLAG_MOTOR_FAULTING) |
  (1 << MOTORON_STATUS_FLAG_NO_POWER) |
  (1 << MOTORON_STATUS_FLAG_ERROR_ACTIVE);

void checkCommunicationError(uint8_t errorCode)
{
  if (errorCode)
  {
    while (1)
    {
      mc.reset();
      Serial.print(F("Communication error: "));
      Serial.println(errorCode);
      delay(1000);
    }
  }
}

void checkControllerError(uint16_t status)
{
  if (status & errorMask)
  {
    while (1)
    {
      // One of the error flags is set.  The Motoron should
      // already be stopping the motors.  We report the issue to
      // the user and send reset commands to be extra careful.
      mc.reset();
      Serial.print(F("Controller error: 0x"));
      Serial.println(status, HEX);
      delay(1000);
    }
  }
}

void checkVinVoltage(uint16_t voltageMv)
{
  if (voltageMv < minVinVoltageMv)
  {
    while (1)
    {
      mc.reset();
      Serial.print(F("VIN voltage too low: "));
      Serial.println(voltageMv);
      delay(1000);
    }
  }
}

void checkForProblems() {
  uint16_t status = mc.getStatusFlags();
  checkCommunicationError(mc.getLastError());
  checkControllerError(status);

  uint32_t voltageMv = mc.getVinVoltageMv(referenceMv, vinType);
  checkCommunicationError(mc.getLastError());
  checkVinVoltage(voltageMv);
}

void setup() {
  Serial.begin(9600);
  Wire.begin();

  mc.reinitialize();
  mc.clearResetFlag();

  mc.setErrorResponse(MOTORON_ERROR_RESPONSE_BRAKE);
  mc.setErrorMask(errorMask);

  mc.setCommandTimeoutMilliseconds(100);

  mc.setMaxAcceleration(1, 200);
  mc.setMaxDeceleration(1, 300);

  mc.setMaxAcceleration(2, 200);
  mc.setMaxDeceleration(2, 300);

  while(mc.getMotorDrivingFlag())
  mc.clearMotorFaultUnconditional();

  pinMode(forward, INPUT_PULLUP);
  pinMode(backward, INPUT_PULLUP);
  pinMode(left, INPUT_PULLUP);
  pinMode(right, INPUT_PULLUP);
}

void loop() {
  checkForProblems();

  if (digitalRead(forward) == 0) {
    mc.setSpeed(1, 190);
    mc.setSpeed(2, 190);
  }

  if (digitalRead(backward) == 0) {
    mc.setSpeed(1, -190);
    mc.setSpeed(2, -190);
  }

  if (digitalRead(left) == 0) {
    mc.setSpeed(1, 100);
    mc.setSpeed(2, -100);
  }

  if (digitalRead(right) == 0) {
    mc.setSpeed(1, 100);
    mc.setSpeed(2, -100);
  }
}
