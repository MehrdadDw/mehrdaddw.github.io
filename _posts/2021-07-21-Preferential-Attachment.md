---
layout: post
title: Preferential Attachment - a brief overview
categories: [Social & Economical Networks, Preferential Attachement]
tags: [Preferential Attachement, Social Networks, Python, Chart]
mermaid: true 
---
<style type="text/css">
   {
    text-align: center;
	
}

.center img {
    display: block;
    margin: 0 auto;
	width:80%;
}

</style>
## Definition


>In this model of network creation, "The rich get richer" or "All are equal but some are more equal!".


### **Algorithm Description**

Each new edge out of m0, is assigned to existing nodes with the chance of coresponding degree
### Step1. creating the **draw pool** of existing nodes based on their degrees:

```python
choices=[node for node in range(current_nodes) for x in range(deg(edges,node))]
```
### Step2. **choose** and repeat choosing proccess for **m0** edges :
```python
for x in range(m0):
    if (len(choices)==0):
        break
    choosen=random.choice(choices)

```

### Step3. Add the edges to network 

```python
#for cont.
  #number of new node
  current_nodes+=1
  edges.append((choosen,current_nodes))
  #ommit the choosen node from the pool
  choices=list(filter(lambda a: a != choosen, choices))
```
The implemented algorithm is based on [Barabási–Albert (BA) model](https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model)
### **Degree Distribution Result**
The degree distribution as it can be guessed is decreasing for higher deegres and is said that the distribution follows power law distribution. The interesting point as shown in chart, is that the lower the m0 the highest degree increases and the highest degree nodes are having a better chance to get higher such that for example the degree of 65ish happens by setting m0=1, while by setting m0=5 the degree is less than 40.
![Preferential attachment]({{site.url}}/../images/Preferential_attachment.png){:class="img-responsive"}
{: .center}
![Preferential attachment vs Random]({{site.url}}/../images/Rand_vs_Preferential_attachment.png){:class="img-responsive"}
{: .center}
[Full code here](https://github.com/Dowlatabadi/HWs/blob/master/SN/preferential_attachment.py)


