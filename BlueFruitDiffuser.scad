/* 
BlueFruit "Snap on" Blast Sheild / Diffuser
Design by Greg Huber (Greg's Maker Corner)
Goal: Diffuse the neopixel lights without getting in the way of board components.
*/
$fn=100;
h=2;

translate([0,0,h/2])
{   difference()
    {
        cylinder(h=h, r=38/2, center=true);
        cylinder(h=h+.1, r=(38-6.75)/2, center=true);   
        
        translate([0,-19,-h/2])
        linear_extrude(h+.1)
        square([10,8], center=true);
    }
}



//JST Cut out / clip
translate([0,-20,0])
{
    difference()
    {
        linear_extrude(h+3)
        square([10,10],center=true);

        translate([0,0,0])
        linear_extrude(h+3.1)
        square([8,12],center=true);
    }
       //hat over JST
        translate([0,0,h+3])
        linear_extrude(h/2)
        square([10,10],center=true);
}




//USB Cut out / clip
translate([0,21,0])
difference()
{
    linear_extrude(h)
    square([10,7],center=true);

    translate([0,0,0])
    linear_extrude(h+.1)
    square([7.75,7],center=true);
}
