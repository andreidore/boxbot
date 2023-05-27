$fn=100;

height_diff=300;
 
 module rcube(size, radius) {
    hull() {
        translate([radius, radius]) cylinder(r = radius, h = size[2]);
        translate([size[0] - radius, radius]) cylinder(r = radius, h = size[2]);
        translate([size[0] - radius, size[1] - radius]) cylinder(r = radius, h = size[2]);
        translate([radius, size[1] - radius]) cylinder(r = radius, h = size[2]);
    }
}





union(){

    difference(){
        
        translate([-200,-200,0]){
              rcube(size=[400,400,100],radius=10);
        }
            
            


        translate([0,0,103]){
            cube(size=[396,396,200],center=true);
        }


        //sub wheel 1
        translate([-170,0,0]){
            cube(size=[20,100,height_diff],center=true);
            
            translate([16.4,15.6,0]){ 
               cylinder(h=height_diff, r=1.6, center=true);
            }
            translate([54.8,15.6,0]){ 
               cylinder(h=height_diff, r=1.6, center=true);
            }

            translate([16.4,-15.6,0]){ 
               cylinder(h=height_diff, r=1.6, center=true);
            }
            translate([54.8,-15.6,0]){ 
               cylinder(h=height_diff, r=1.6, center=true);
            }
            
        }



         
        //sub wheel 2
        translate([170,0,0]){
            cube(size=[26,100,height_diff],center=true);
            
            translate([-16.4,15.6,0]){ 
               cylinder(h=height_diff, r=1.6, center=true, $fn=100);
            }
            translate([-54.8,15.6,0]){ 
               cylinder(h=height_diff, r=1.6, center=true, $fn=100);
            }

            translate([-16.4,-15.6,0]){ 
               cylinder(h=height_diff, r=1.6, center=true, $fn=100);
            }
            translate([-54.8,-15.6,0]){ 
               cylinder(h=height_diff, r=1.6, center=true, $fn=100);
            }
            
        }





        //spacer

        translate([-193,193,0]){ 
             cylinder(h=height_diff, r=1.6, center=true);
        }

        translate([193,193,0]){ 
             cylinder(h=height_diff, r=1.6, center=true);
        }

        translate([193,-193,0]){ 
             cylinder(h=height_diff, r=1.6, center=true);
        }

        translate([-193,-193,0]){ 
             cylinder(h=height_diff, r=1.6, center=true);
        }




        // ball caster 1

        translate([0,-140,0]){
         cube(size=[90,90,height_diff],center=true);
        }


        // ball caster 2

        translate([0,140,0]){
         cube(size=[90,90,height_diff],center=true);
        }





        // power battery

        translate([0,-33.5,0]){ 
             cylinder(h=20, r=1.3, center=true, $fn=100);
        }

        translate([0,33.5,0]){ 
             cylinder(h=20, r=1.3, center=true, $fn=100);
        }





        //cube(size=[200,200,20],center=true);

        translate([-120,120,0]){
         cube(size=[100,100,20],center=true);
        }

        //translate([35,0,0]){
        // cube(size=[40,100,20],center=true);
        //}

    }
    
    difference(){
        translate([-193.6,193.6,0]){
           cylinder(h=100,r=5);
        }
    
       translate([-193,193,0]){ 
             cylinder(h=height_diff, r=2.6, center=true);
        }
    
    }
    
    
    
}