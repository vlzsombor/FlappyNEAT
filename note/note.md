```
__init__ (c:\git\personal\FlappyNEAT\game\Bird.py:28)
	__init__ (c:\git\personal\FlappyNEAT\game\population.py:20)
		<module> (c:\git\personal\FlappyNEAT\__main__.py:53)
```

`(c:\git\personal\FlappyNEAT\__main__.py:53)` => self.brain = Genome(gh)

**Bird.py itself sets the "brain"**

##### Decision:

```
think (c:\git\personal\FlappyNEAT\game\Bird.py:123)
update (c:\git\personal\FlappyNEAT\game\Bird.py:91)
update (c:\git\personal\FlappyNEAT\game\population.py:56)
main (c:\git\personal\FlappyNEAT\__main__.py:173)
menu (c:\git\personal\FlappyNEAT\__main__.py:231)
<module> (c:\git\personal\FlappyNEAT\__main__.py:238)
```

```python
        outs = self.brain.get_outputs(inputs)
        # use outputs to flap or not
        if outs[1] > outs[0]:
            should_flap = True
        return should_flap
```



```
update (c:\git\personal\FlappyNEAT\game\Bird.py:103)
update (c:\git\personal\FlappyNEAT\game\population.py:56)
main (c:\git\personal\FlappyNEAT\__main__.py:173)
menu (c:\git\personal\FlappyNEAT\__main__.py:231)
<module> (c:\git\personal\FlappyNEAT\__main__.py:238)
```

```python
# flap
if up or (_input and not self.flap and self.rect.y > 0 and self.alive):
	self.flap = True
	self.vel = -7
```




```
show (c:\git\personal\FlappyNEAT\neat\genome.py:343)
main (c:\git\personal\FlappyNEAT\__main__.py:182)
menu (c:\git\personal\FlappyNEAT\__main__.py:231)
<module> (c:\git\personal\FlappyNEAT\__main__.py:238)
```

Show wtf is this method??
Genome.show() ? What does this do? Maybe showing in the diagram right top?



### Neat algorithm pillars:

* Fitness calculation.
* Killing not effective birds
* Get the most effective species and breed them

```
main (c:\git\personal\FlappyNEAT\__main__.py:173)
menu (c:\git\personal\FlappyNEAT\__main__.py:231)
<module> (c:\git\personal\FlappyNEAT\__main__.py:238)
```

Breeding:
`Bird: def mate(self, partner):` => `brain def crossover(self, partner)`

* Neural network?: 
 Forward propagation:
```get_outputs (c:\git\personal\FlappyNEAT\neat\genome.py:157)
think (c:\git\personal\FlappyNEAT\game\Bird.py:129)
update (c:\git\personal\FlappyNEAT\game\Bird.py:91)
update (c:\git\personal\FlappyNEAT\game\population.py:56)
main (c:\git\personal\FlappyNEAT\__main__.py:173)
menu (c:\git\personal\FlappyNEAT\__main__.py:231)
<module> (c:\git\personal\FlappyNEAT\__main__.py:238) 

        self.output = self.sigmoid(s)
```


Backpropagation? 

Is there backpropagation? [url](https://ai.stackexchange.com/questions/5586/does-training-happen-during-neat)
![[1_Oh572O-xjD8eDaw_NIjpDg.png]]



![[0_0qt5O-9iHj6PVMPm.png]]


![[Frame-13.png]]