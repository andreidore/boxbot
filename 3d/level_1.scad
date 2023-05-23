module rounded_square( width, radius_corner ) {
	translate( [ radius_corner, radius_corner, 0 ] )
		minkowski() {
			square( width - 2 * radius_corner,center=true );
			circle( radius_corner );
		}
}
   

module rcube(size, radius) {
    hull() {
        translate([radius, radius]) cylinder(r = radius, h = size[2]);
        translate([size[0] - radius, radius]) cylinder(r = radius, h = size[2]);
        translate([size[0] - radius, size[1] - radius]) cylinder(r = radius, h = size[2]);
        translate([radius, size[1] - radius]) cylinder(r = radius, h = size[2]);
    }
}

difference(){
//cylinder(h=3, r=100, center=true, $fn=100);
    
//linear_extrude(3){
// rounded_square(220,10);
//}
//cube(size=[200,200,3],center=true);
translate([-100,-100,0]){
 rcube(size=[200,200,3],radius=10);
}


//sub wheel 1
translate([-90,0,0]){
    cube(size=[16,100,20],center=true);
    
    translate([16.4,15.6,0]){ 
       cylinder(h=20, r=1.6, center=true, $fn=100);
    }
    translate([54.8,15.6,0]){ 
       cylinder(h=20, r=1.6, center=true, $fn=100);
    }

    translate([16.4,-15.6,0]){ 
       cylinder(h=20, r=1.6, center=true, $fn=100);
    }
    translate([54.8,-15.6,0]){ 
       cylinder(h=20, r=1.6, center=true, $fn=100);
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

//translate([-35,0,0]){
// cube(size=[40,100,20],center=true);
//}

//translate([35,0,0]){
// cube(size=[40,100,20],center=true);
//}

}