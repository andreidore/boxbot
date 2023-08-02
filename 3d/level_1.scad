$fn=100;

height_diff=300;
 
 
module l_bracket(){
    
    for ( i = [0 : 6] ){    
        translate([8.4+i*6.4,15.6,0]){ 
            cylinder(h=height_diff, r=1.6, center=true);
        }    
     }
     
     for ( i = [0 : 6] ){    
        translate([8.4+i*6.4,-15.6,0]){ 
            cylinder(h=height_diff, r=1.6, center=true);
        }    
     }
    
}


module ballcaster(){
    
    translate([-29/2,29/2,0]){ 
         cylinder(h=height_diff, r=2.6, center=true);
    }
    translate([29/2,29/2,0]){ 
        cylinder(h=height_diff, r=2.6, center=true);
    }
    translate([29/2,-29/2,0]){ 
        cylinder(h=height_diff, r=2.6, center=true);
    }
    translate([-29/2,-29/2,0]){ 
        cylinder(h=height_diff, r=2.6, center=true);
    }
    
    
}


module segment(){
    
    translate([50,0,0]){
        cylinder(h=height_diff, r=2.6, center=true, $fn=100);
    }
    
    translate([152,0,0]){
        cylinder(h=height_diff, r=2.6, center=true, $fn=100);
    }
    
    
}



difference(){
    
    translate([-200,-200,0]){
          cube(size=[400,400,4]);
    }
        
        
    //wheel 1
    translate([-160,0,0]){
        cube(size=[40,160,height_diff],center=true);
    }
    
    translate([-140,0,0]){
        l_bracket();
    }


    


     
    //sub wheel 2
    translate([160,0,0]){
        cube(size=[40,160,height_diff],center=true);
    }
    
    translate([140-53.2,0,0]){
        l_bracket();
    }




    //ball caster 1

    translate([-150,145,0]){
        ballcaster();       
    }


    // ball caster 2
    translate([150,145,0]){
        ballcaster();       
    }
    
    // ball caster 3
    translate([150,-145,0]){
        ballcaster();       
    }
    
     // ball caster 4
    translate([-150,-145,0]){
        ballcaster();       
    }
    
    
    // frame screws
    // 1
   
    translate([-190,190,0]){
        segment();
    }
    
    
    
    translate([-190,0,0]){
        rotate([0,0, 90]){
           segment();
        }
    }
    
     translate([-10,0,0]){
        rotate([0,0,90]){
           segment();
        }
    }
    
    
    // 2
   
    translate([0,190,0]){
        segment();
    }
    
    
    translate([190,0,0]){
        rotate([0,0,90]){
           segment();
        }
    }
    
     translate([10,0,0]){
        rotate([0,0,90]){
           segment();
        }
    }
    
    
    // 3
   
    translate([0,-190,0]){
        segment();
    }
    
    
    translate([190,0,0]){
        rotate([0,0,-90]){
           segment();
        }
    }
    
     translate([10,0,0]){
        rotate([0,0,-90]){
           segment();
        }
    }
    
    
    // 3
   
    translate([-190,-190,0]){
        segment();
    }
    
    
    translate([-190,0,0]){
        rotate([0,0,-90]){
           segment();
        }
    }
    
     translate([-10,0,0]){
        rotate([0,0,-90]){
           segment();
        }
    }
    
    
    //---------
     
    
    
    
    translate([-200,200,0]){
        cube(size=[40,40,height_diff],center=true);
    }
    
    translate([200,200,0]){
        cube(size=[40,40,height_diff],center=true);
    }
    
    translate([200,-200,0]){
        cube(size=[40,40,height_diff],center=true);
    }
    
    translate([-200,-200,0]){
        cube(size=[40,40,height_diff],center=true);
    }
    





    // power battery

    translate([0,-33.5,0]){ 
         cylinder(h=20, r=1.3, center=true, $fn=100);
    }

    translate([0,33.5,0]){ 
         cylinder(h=20, r=1.3, center=true, $fn=100);
    }





    //cube(size=[200,200,20],center=true);

    //translate([-120,120,0]){
    // cube(size=[100,100,20],center=true);
    //}

    //translate([35,0,0]){
    // cube(size=[40,100,20],center=true);
    //}

}




