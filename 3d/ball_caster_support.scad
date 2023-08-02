$fn=100;

h=4;

difference(){
    
     cube([40,40,14],center=true);

    
    translate([-29/2,29/2,0]){ 
         cylinder(h=20, r=2.6, center=true);
    }
    translate([29/2,29/2,0]){ 
        cylinder(h=20, r=2.6, center=true);
    }
    translate([29/2,-29/2,0]){ 
        cylinder(h=20, r=2.6, center=true);
    }
    translate([-29/2,-29/2,0]){ 
        cylinder(h=20, r=2.6, center=true);
    }
    
    
}



