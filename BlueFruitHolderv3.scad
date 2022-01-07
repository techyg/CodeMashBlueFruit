// This holder is designed for the Bluefruit Low Energy Circuit Playground (Adafruit).
// Designed by Greg Huber

$fn=100;

x=23;
anglez=40;
z=3;

module peg(x,y,z,ht)
{

    translate([x,y,z])
    cylinder(r=5/2, h=ht);
    
    translate([x,y,z])
    cylinder(r=2.75/2, h=ht+3);

}


module holder()
{
    //base
    cylinder(r=55/2, h=3);
    rotate([0,0,90])  //rotate so USB/JST conncetors are on the side
    {
//        peg(x,0,z,3);
//        peg(-x,0,z,3);
        rotate([0,0,anglez]) peg(x,0,z,3);
        rotate([0,0,-anglez]) peg(-x,0,z,3);
        rotate([0,0,anglez]) peg(-x,0,z,3);
        rotate([0,0,-anglez]) peg(x,0,z,3);       
    } 
}

module base()
{        
    scale([1.5,1,1])cylinder(r=60/2, h=5);

    //Create a support for back of holder 
    hull()
    {    
        translate([0,-8,4])
        linear_extrude(5)
        square([25,10],center=true);

        translate([0,-6,8])
        linear_extrude(5)
        square([15,5],center=true);
        
        translate([0,-4,10])
        linear_extrude(5)
        square([10,4],center=true);
    }       
}

module buildholder()
{
    translate([0,0,26])
    rotate([60,0,0])holder(); 
    base();
}

buildholder();