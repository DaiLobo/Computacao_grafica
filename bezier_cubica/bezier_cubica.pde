boolean arrastandoA = false;
boolean arrastandoB = false;
boolean arrastandoC = false;
boolean arrastandoD = false;
  
float p1x = 160;
float p1y = 300;

float p2x = 320;
float p2y = 300;

float p3x = 480;
float p3y = 300;

float p4x = 640;
float p4y = 300;

void setup()
{
  size(800,600);
}

void draw()
{
  background(42, 35, 89);

  noFill();
  stroke(217, 115, 26);
  beginShape();
    vertex(p1x, p1y);
    for(float t = 0; t <= 1; t += 0.05)
    {
      float ax = p1x + t*(p2x-p1x);
      float ay = p1y + t*(p2y-p1y);
      
      float bx = p2x + t*(p3x-p2x);
      float by = p2y + t*(p3y-p2y);
      
      float cx = p3x + t*(p4x - p3x);
      float cy = p3y + t*(p4y - p3y);
       
      //Reta entre a e b
      float dx = ax + t*(bx - ax);
      float dy = ay + t*(by - ay);
      
      //Reta entre b e c
      float ex = bx + t*(cx - bx);
      float ey = by + t*(cy - by);
      
      //Reta entre d e e
      float fx = dx + t*(ex - dx); 
      float fy = dy + t*(ey - dy);
      
      vertex(fx,fy);  
    }
    vertex(p4x, p4y);
    
  endShape();
  
  fill(191, 36, 122);
  noStroke();
  circle(p1x, p1y,10);
  circle(p2x, p2y,10);
  circle(p3x, p3y,10);
  circle(p4x, p4y,10);
   
     
  if (mousePressed == true) {
   if(dist(p1x, p1y, mouseX, mouseY)<10){
    arrastandoA = true;
   }
   if(dist(p2x, p2y, mouseX, mouseY)<10){
    arrastandoB = true;
   }
   if(dist(p3x, p3y, mouseX, mouseY)<10){
    arrastandoC = true;
   }
   if(dist(p4x, p4y, mouseX, mouseY)<10){
    arrastandoD = true;
   }
  }
  
  if(arrastandoA)
  {
    p1x = mouseX;
    p1y = mouseY;
  }
  else if(arrastandoB)
  {
    p2x = mouseX;
    p2y = mouseY;
  }
  else if(arrastandoC)
  {
    p3x = mouseX;
    p3y = mouseY;
  }
  else if(arrastandoD)
  {
    p4x = mouseX;
    p4y = mouseY;
  }
  
  
}

void mouseReleased(){
  arrastandoA = false;
  arrastandoB = false;
  arrastandoC = false;
  arrastandoD = false;
}
