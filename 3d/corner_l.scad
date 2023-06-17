$fn=100;

height=2;
height_diff=16;



difference(){
    union(){
        cube(size=[40,20,height]);
        cube(size=[20,40,height]);
    }
    
    translate([10,10,0]){
     cylinder(h=height_diff, r=2.6, center=true);
    }
    
    translate([10,30,0]){
     cylinder(h=height_diff, r=2.6, center=true);
    }
    
    translate([30,10,0]){
     cylinder(h=height_diff, r=2.6, center=true);
    }
}
    