

difference(){
    cylinder(h=3, r=200, center=true, $fn=100);






    // arduino
    
    //translate([-33,-25.4,0]){
        
     translate([-25.4,-17.76,0]){     
           cylinder(h=20, r=1.6, center=true, $fn=100);
     }
    
     translate([-17.78,33,0]){ 
           cylinder(h=20, r=1.6, center=true, $fn=100);
     }
     
     translate([17.78,33,0]){ 
           cylinder(h=20, r=1.6, center=true, $fn=100);
     }  
    //}
    
    
    
    //cable
    translate([0,60,0]){
        
       cube(size=[70,30,20],center=true);
            
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
    
    
    
    
    
    
    translate([0,-50,0]){
     cube(size=[100,25,20],center=true);
    }
    
    
    
}

    
    







   

