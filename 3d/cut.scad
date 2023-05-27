 model="level_1.stl";
 
 
 intersection(){
     import(model, convexity=3);
     
     //1
     translate([-200,0,0]){
       cube(size=[200,200,400]);
     }
     
     //2
     //translate([0,0,0]){
     //   cube(size=[200,200,10]);
     //}
     
     //3
     //translate([0,0,0]){
     //   cube(size=[200,200,10]);
     //}
     
     
     //4
     //translate([-200,-200,0]){
    //    cube(size=[200,200,10]);
    // }
     
 }
 
 