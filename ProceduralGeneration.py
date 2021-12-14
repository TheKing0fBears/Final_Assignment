nosie_scale = .002

def start():
  size(1000,750)
  
  background(255,255,255)
  
  for x in range(1000):
    for y in range(750):
      stroke(0,0,0,255.0*noise(x*noise_scale, y*noise_scale))
      point(x,y)

      pen
