float p2x = 100;
float p2y = 250;
boolean arrastandoP = false;
float p3x = 700;
float p3y = 250;
boolean arrastandoQ = false;


void setup(){
  size(800,600);
}

void draw(){
  background(150); //cor na escala de cinza
  
  float p1x = 100; //coordenada do primeiro ponto
  float p1y = 250;
  
  if(arrastandoP)
  {
    p2x = mouseX;
    p2y = mouseY;
  }
  else if(arrastandoQ)
  {
    p3x = mouseX;
    p3y = mouseY;
  }
  
  circle(p2x, p2y,10);
  circle(p3x, p3y,10);

  float p4x = 700; //coordenada do ultimo ponto
  float p4y = 250;
  
  beginShape(); // grava os vertex p forma
  vertex(p1x, p1y); //a partir do primeiro ponto
  for(float t = 0; t <= 1; t += 0.01)
  {
    float ax = p1x + t*(p2x-p1x);
    float bx = p2x + t*(p3x-p2x);
   // float cx = p3x + t*(p4x-p3x); 
    float dx = ax + t*(bx-ax);
    
    float ay = p1y + t*(p2y-p1y);
    float by = p2y + t*(p3y-p2y);
   // float cy = p3y + t*(p4y-p3y);   
    float dy = ay + t*(by-ay);
    vertex(dx,dy);  
  }
  vertex(p4x, p4y);
  endShape(CLOSE);
}

void mousePressed()
{
    if(dist(p2x, p2y, mouseX, mouseY)<10)
    {
      arrastandoP = true;
    }
    if(dist(p3x, p3y, mouseX, mouseY)<10)
    {
      arrastandoQ = true;
    }
  
}

void mouseReleased()
{
  arrastandoP = false;
  arrastandoQ = false;
}
