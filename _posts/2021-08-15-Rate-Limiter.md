---
layout: post
title: Rate Limiter System 
categories: [System Desing, Rate Limiter System]
tags: [System Desing, Distributed system, token bucket algorithm, Algorithm, Python]
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
## Problem Definition


>Our service can receive requests and it hands out requests to another external service but the external service is accepting a **limited rate** of requests and the rest are being discarded.

> We what to apply the rate limitation to our service to gain a **high ratio of success**.
Another problem can be a limitation of the **user's requests** rate, such that each user has his **specific limitation**.



System Flow Chart:
```mermaid

graph LR;
    A((user1))-->|N1 requests| Z(API Access Point);
    B((user2))-->|N2 requests| Z(API Access Point);
    C((user3))-->|N3 requests| Z(API Access Point);
    D((user4))-->|N4 requests| Z(API Access Point);
    E((user5))-->|N5 requests| Z(API Access Point);
    Z(Rate Limiter Service)-->|M1+M2+M3+M4+M5 requests| External(External API);
        Z(Rate Limiter Service)-->|X1+X2+X3+X4+X5 requests| Discard(Discard);
```

## Solution:

The **trivial solution** is to define a back-off time between 2 batches of requests, but it has two main problems: 
- The rate can exceed the limit 
- Even by choosing slots little enough, still, the issue might remain or might result in another performance problem.


The rate-limiting problem is not a new problem. There are many solutions but the **token bucket algorithm** is a simple solution that would be investigated in this post.


### Algorithm Description:

The **actual algorithm** is more like **discrete event simulation**; such that in each occurrence of events we decide for the new state of the system. The main event is: *the request arrival*.
in which we first add newly generated tokens within the gap between last token usage and now.

Then we investigate for required tokens(units that show the ability to execute one request). Therefore the decision can be to discard the request or pass it to the service.


If the total requests for the users should be limited, we can use a cached HashSet for the user's tokens, and last req timestamp, and the limit value.

Rate Limiter Logic:
```mermaid

graph LR;
    A((on Arrival))-->|Clculate Tokens| Z(API Access Point);
    Z(Are tokens available?)-->|Yes| External(Service-Approved);
        Z(Are tokens available?)-->|No| Denied(Service-Denied);

```


### on Request Arrival:

```python
    def RefillandExamine(user,request_tokens):
        #refill
        now=Datetime.time
        current_tokens=current_tokens+(now-last_timestamp)*fill_rate
        #decision point
        if (current_tokens>=request_tokens):
            current_tokens-=request_tokens
        else:
            discard_request()

```




In a distributed system we still can calculate the sum of requests, but to ensure we have enough tokens in each bucket, we assign `N*required_tokens` to overall nodes but after each event we clear exessive tokens. In this case we need to inform nodes about each other that it can be acheived by using fully mesh broadcasting, **Gossip Communication**, **Distributed Cache** or **Leader Election** and coordination methods.


In this situation, we risk the consumption of excessive tokens, but it can be fixed.


