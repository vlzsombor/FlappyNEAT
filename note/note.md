n_outputs = 2  -> up, do nothing

```
__init__ (c:\git\personal\FlappyNEAT\game\Bird.py:28)
	__init__ (c:\git\personal\FlappyNEAT\game\population.py:20)
		<module> (c:\git\personal\FlappyNEAT\__main__.py:53)
```

`(c:\git\personal\FlappyNEAT\__main__.py:53)` => self.brain = Genome(gh)

**Bird.py itself sets the "brain"**

##### Decision:





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
How breeding happening? What does it mean python-wise? Two lists are merged? Something with nodes happening...
```
crossover (c:\git\personal\FlappyNEAT\neat\genome.py:192)
mate (c:\git\personal\FlappyNEAT\game\Bird.py:41)
reset (c:\git\personal\FlappyNEAT\game\population.py:44)
reset (c:\git\personal\FlappyNEAT\__main__.py:71)
main (c:\git\personal\FlappyNEAT\__main__.py:140)
menu (c:\git\personal\FlappyNEAT\__main__.py:231)
<module> (c:\git\personal\FlappyNEAT\__main__.py:238)
        # Give the child the maximum nodes of the two ??
```


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
gene.py genom.py difference?

**Genome is the sum of all genetic material in an individual. It provides all information about the organism and directs all vital processes.**

| gene                                                                                       | Comment                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| innovation id                                                                              | <br>        highest_inno = (<br><br>            p1_highest_inno if self.fitness > partner.fitness else p2_highest_inno<br><br>        )<br><br>*The innovation numbers are historical markers that identify the original his-<br>torical ancestor of each gene* |
| There are weights, I think, this object is closer to the neural network representation (?) |                                                                                                                                                                                                                                                                 |
|                                                                                            |                                                                                                                                                                                                                                                                 |
|                                                                                            |                                                                                                                                                                                                                                                                 |

Process:

```
connect_nodes (c:\git\personal\FlappyNEAT\neat\genome.py:80)
add_gene (c:\git\personal\FlappyNEAT\neat\genome.py:93)
mutate (c:\git\personal\FlappyNEAT\neat\genome.py:99)
__init__ (c:\git\personal\FlappyNEAT\game\Bird.py:31)
__init__ (c:\git\personal\FlappyNEAT\game\population.py:20)
<module> (c:\git\personal\FlappyNEAT\__main__.py:53)
```



WTFs:
wtf is that graph ??
![[Pasted image 20250107114052.png]]

Input:
```python
class Bird:
    def get_inputs(self, closest):
        inputs = []
        inputs.append((y_pos_ground - self.rect.y) / win_height)  # bird height
        inputs.append((closest.xPos - self.rect.x) / win_width)  # Dist from pipe
        inputs.append(
            (closest.topPos - self.rect.y) / win_height
        )  # Dist from bird to top Pipe
        inputs.append(
            (self.rect.y - closest.bottomPos) / win_height
        )  # Dist from bird to bottom Pipe
        return inputs
```

output:
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



* When will the gene disabled? How is it represented in the python code? => `class Gene: self.enabled`
* What does weight do? (in Gene class)
Gene history is crucial:
*There needed to be some way to keep crossover orderly, so that the right genes could*
*be crossed with the right genes.*


```python
    def mutate(self):
        # initialization:
        if len(self.genes) == 0:
            self.add_gene()
        if random.random() < 0.8:
            for i in range(len(self.genes)):
                self.genes[i].mutate()
        if random.random() < 0.08:
            self.add_gene()
        if random.random() < 0.02:
            self.add_node()
        pass
```
this seems to be important ⬆️

Backpropagation?  
Is there backpropagation? [url](https://ai.stackexchange.com/questions/5586/does-training-happen-during-neat)
No there is no backpropagation in NEAT algorithm. _NEAT replaces typical back propagation with a genetic algorithm_
[Reddit comments](https://www.reddit.com/r/learnprogramming/comments/11btct3/where_to_start_learning_the_neat_algorithm/)
![[1_Oh572O-xjD8eDaw_NIjpDg.png]]



Backpropagation is an optimization of the neural network.
NEAT or genetic algorithms use "mutation and merging/etc" as optimization.










  
0 =0.39166666666666666

1 =0.8421052631578947

2 =0.0125

3 =-0.1375