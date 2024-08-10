---
title: "Genetic Algorithm - Solving Assignment to Demographics"
tags:
  - Python
  - Machine Learning
  - Artificial Intelligence
  - Genetic Algorithm
  
header:
  teaser: https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/genetic-algo/gen4.png
  og_image: https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/genetic-algo/gen4.png
 
---

{% raw %}
<body>
    <H1>Introduction</H1>

    I worked at a marketing tech company, and they ran into this real-world problem. I managed to solve it with a Genetic Algorithm. In the post, I'll try to describe the problem and how I solved it. Linked at the end is a Jupyter notebook that you can play around with. 

    <br>
    <H1>Problem Statement</H1>
    

    <h2>The Business</h2>
    I worked with an "IHUT" company (In-House Usage Testing). We had about 50,000 users to whom we would ship physical boxes containing some product. Those people would test out those products, and then give us their feedback. 
    It allowed companies to test out products prior to releasing them to the greater public. 


    <h2>The Challenge</h2>
    These companies would often wish to get results / analytics from a variety of different specific groups. Additionally, the product / box might need to be prepared differently for different groups. 
    The problem is that each of the demographics that we're targeting to send boxes to might not be mutually exclusive. Examples of demographics include age, gender, employment status, education level, preferences, etc.

    Let's use the following example.
    Say the customer is a pet-food company. They want to test out a new type of pet food. Each person can only receive 1 box. Say our target demographics are 1) People with Birds 2) People with Cats and 3) People with Dogs. 
    Then say we need to ship 100 Dog-Food Boxes to people with Dogs, 50 Cat-Food Boxes to people with Cats, and 50 Bird-Food boxes to people with Birds.

    The problem is, if you look at our sample of people, there are people who have both dogs AND cats, or birds and dogs, etc. This means that if we wish to select from our pool of demographics in order to allocate a box to that person, we could potentially <strong>run out of people in that particular demographic</strong>

    So, it's a constraint satisfaction problem. This is a toy example, but in the real world, we could have 10 or 15 competing demographics, so optimization can be incredibly challenging. A search algorithm is unlikely to succeed here.

<img src="https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/genetic-algo/gen1.png" style="display: block; margin: 0 auto;" alt="Demographic Selection Constraint Satisfaction Problem">


    <h1>Genetic Algorithms</h1>
<img src="https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/genetic-algo/gen5.png" style="display: block; margin: 0 auto;">
    <img src="https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/genetic-algo/gen6.png" style="display: block; margin: 0 auto;">

    <h1>Solution</H1>
    I employed a genetic algorithm here. The steps are as follows:
    1. First you create a list for each person, which of the 3 buckets (demographics) they can possibly be in.
    2. Next, you create a full assignment to fill each of the buckets. That is, you randomly "choose" which bucket a person will fall into. You do this N times (N = your population size)
    3. Compute a fitness function. Your fitness might be average of how "full" your buckets are. For example, if you have 80/100 in the first bucket, 50/50 in the second, and 45/50 in the third, your fitness would compute to 0.95%.
    4. You then "cull" or kill off some percentage of those (say, 90%). You can modify these parameters.
    5. You then repopulate up to N (population) using a combination of Mutation and Crossover. 

<img src="https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/genetic-algo/gen4.png" style="display: block; margin: 0 auto;">
<img src="https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/genetic-algo/gen3.png" style="display: block; margin: 0 auto;">
<img src="https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/genetic-algo/gen2.png" style="display: block; margin: 0 auto; width: 50%;">


</body>
{% endraw %}
