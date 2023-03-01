from schemdraw import Drawing
from schemdraw import flow
from schemdraw import dsp

with Drawing() as d:
    d += (QAM := flow.Box(w=2.5, h=1.5).label("QAM \n Mapping").fill('lightblue'))
    d += flow.Arrow().right().at(QAM.E).label('Serial \n To Parallel')
    
    d += (IFFT := flow.Box(w=2.5, h=1.5).anchor('W').label('IFFT').fill('lightblue'))
    d += flow.Arrow().right().at(IFFT.E).label('Parallel \n To Serial')
    
    d += (PREFIX := flow.Box(w=2.5, h=1.5).anchor('W').label('add \n prefix').fill('lightblue'))
    d += flow.Arrow().down(d.unit/2).at(PREFIX.S)
    
    d += (CHANNEL := dsp.Box(w=2.5, h=1.5).anchor('N').label('Channel $H$'))
    d += flow.Arrow().down(d.unit/4).at(CHANNEL.S)
    
    d += (SUM := dsp.Sum().anchor('W').fill('navajowhite'))
    d += flow.Arrow().down(d.unit/4).at(SUM.E)
    
    d += (AWGN := dsp.Box(w=2.5, h=1.5).label('$N(\mu,\sigma^2)$'))
    #d += flow.Arrow().at(AWGN.E).tox(SUM.S)
