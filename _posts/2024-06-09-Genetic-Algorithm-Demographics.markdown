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
<body style="font-family: Arial, sans-serif; line-height: 1.6; margin: 20px;">

    <header>
        <h1 style="text-align: center; color: #2c3e50; font-size: 2.5em;">Introduction</h1>
        <p style="text-align: justify; font-size: 1.2em;">
            I worked at a marketing tech company where we encountered a challenging real-world problem. I successfully solved it using a Genetic Algorithm. In this post, I'll describe the problem and the solution I implemented. A Jupyter notebook is linked at the end for you to explore further.
        </p>
    </header>

    <section>
        <h1 style="color: #2c3e50; font-size: 2em;">Problem Statement</h1>
        <h2 style="color: #2980b9;">The Business</h2>
        <p style="text-align: justify; font-size: 1.1em;">
            I worked with an "IHUT" (In-House Usage Testing) company that managed a user base of about 50,000 individuals. These users were sent physical boxes containing products to test. They would then provide feedback, allowing companies to test products before a broader public release.
        </p>

        <h2 style="color: #2980b9;">The Challenge</h2>
        <p style="text-align: justify; font-size: 1.1em;">
            Companies often sought analytics from various specific groups, with the potential need for different box preparations for each group. The issue arose because these target demographics were not mutually exclusive. Demographics might include factors like age, gender, employment status, education level, and preferences.
        </p>
        <p style="text-align: justify; font-size: 1.1em;">
            For example, consider a pet-food company wanting to test a new pet food type. We might need to ship 100 Dog-Food Boxes to people with dogs, 50 Cat-Food Boxes to people with cats, and 50 Bird-Food Boxes to people with birds. However, some individuals might own both dogs and cats or other combinations, leading to a potential shortage in specific demographics. This situation presents a constraint satisfaction problem.
        </p>
        <p style="text-align: justify; font-size: 1.1em;">
            In the real world, the challenge scales with more competing demographics, making optimization complex and traditional search algorithms less effective.
        </p>
        <figure style="text-align: center;">
            <img src="https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/genetic-algo/gen1.png" alt="Demographic Selection Constraint Satisfaction Problem" style="max-width: 100%; height: auto; margin: 20px auto;">
            <figcaption style="font-size: 0.9em; color: #7f8c8d;">Figure: Demographic Selection Constraint Satisfaction Problem</figcaption>
        </figure>
    </section>

    <section>
        <h1 style="color: #2c3e50; font-size: 2em;">Genetic Algorithms</h1>
        <figure style="text-align: center;">
            <img src="https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/genetic-algo/gen5.png" alt="Genetic Algorithm Process" style="max-width: 100%; height: auto; margin: 20px auto;">
            <img src="https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/genetic-algo/gen6.png" alt="Genetic Algorithm in Action" style="max-width: 100%; height: auto; margin: 20px auto;">
        </figure>
    </section>

    <section>
        <h1 style="color: #2c3e50; font-size: 2em;">Solution</h1>
        <p style="text-align: justify; font-size: 1.1em;">
            I applied a genetic algorithm to tackle this problem. The process involved the following steps:
        </p>
        <ol style="font-size: 1.1em; margin-left: 20px;">
            <li>Create a list for each person indicating which of the three demographics they belong to.</li>
            <li>Randomly assign individuals to these demographics N times (N = population size).</li>
            <li>Compute a fitness function based on how "full" each demographic bucket is.</li>
            <li>Cull a percentage of the population based on fitness (e.g., the bottom 90%).</li>
            <li>Repopulate the population through mutation and crossover until you reach the original population size.</li>
        </ol>
        <figure style="text-align: center;">
            <img src="https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/genetic-algo/gen4.png" alt="Genetic Algorithm Results" style="max-width: 100%; height: auto; margin: 20px auto;">
            <img src="https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/genetic-algo/gen3.png" alt="Genetic Algorithm Process" style="max-width: 100%; height: auto; margin: 20px auto;">
            <img src="https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/genetic-algo/gen2.png" alt="Genetic Algorithm Flowchart" style="max-width: 50%; height: auto; margin: 20px auto;">
        </figure>
    </section>

</body>
{% endraw %}
