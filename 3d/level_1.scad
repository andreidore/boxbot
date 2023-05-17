
   

difference(){
cylinder(h=3, r=100, center=true, $fn=100);

translate([-100,0,0]){
    cube(size=[30,40,20],center=true);
    
    translate([28.05,9,0]){ 
       cylinder(h=20, r=1.3, center=true, $fn=100);
    }

    translate([28.05,-9,0]){ 
       cylinder(h=20, r=1.3, center=true, $fn=100);
    } 
    
}



 
translate([100,0,0]){
    cube(size=[30,40,20],center=true);

    translate([-28.05,9,0]){ 
       cylinder(h=20, r=1.3, center=true, $fn=100);
    }

    translate([-28.05,-9,0]){ 
       cylinder(h=20, r=1.3, center=true, $fn=100);
    }     
}



// ballcaster

translate([0,-90,0]){
    

    translate([0,14.5,0]){ 
       cylinder(h=20, r=1.3, center=true, $fn=100);
    }

    translate([0,1,0]){ 
       cylinder(h=20, r=1.3, center=true, $fn=100);
    }     
}





//spacer

translate([65,65,0]){ 
     cylinder(h=20, r=1.6, center=true, $fn=100);
}

translate([65,-65,0]){ 
     cylinder(h=20, r=1.6, center=true, $fn=100);
}

translate([-65,-65,0]){ 
     cylinder(h=20, r=1.6, center=true, $fn=100);
}

translate([-65,65,0]){ 
     cylinder(h=20, r=1.6, center=true, $fn=100);
}



// power battery

translate([0,-33.5,0]){ 
     cylinder(h=20, r=1.3, center=true, $fn=100);
}

translate([0,33.5,0]){ 
     cylinder(h=20, r=1.3, center=true, $fn=100);
}





//cube(size=[100,40,20],center=true);

translate([-35,0,0]){
 cube(size=[40,100,20],center=true);
}

translate([35,0,0]){
 cube(size=[40,100,20],center=true);
}

}