$fn=100;

h=4;

difference(){

    union(){
        cube([10,50,h]);
        translate([10-h,0,0]){
            cube([h,50,10]);
        }
        translate([10-h,0,10-h]){
            cube([90,50,h]);
        }
        translate([100-h,0,0]){
            cube([h,50,10]);
        }
        translate([100-h,0,0]){
            cube([20,50,h]);
        }
    }
    
    translate([35,10,-3]){
        cylinder(h=30,r=2.6);
    }
  
    translate([35,40,-3]){
        cylinder(h=30,r=2.6);
    }
    
    translate([65,10,-3]){
        cylinder(h=30,r=2.6);
    }
  
    translate([65,40,-3]){
        cylinder(h=30,r=2.6);
    }
    
    
    
    translate([3,25,-3]){
        cylinder(h=30,r=1.6);
    }
    
    
    translate([110,10,-3]){
        cylinder(h=30,r=1.6);
    }
    
    translate([110,40,-3]){
        cylinder(h=30,r=1.6);
    }
    
    
}



