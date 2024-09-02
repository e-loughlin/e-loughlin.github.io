---
title: "Reinforcement Learning - An Exploration"
tags:
  - Engineering
  - Machine Learning
  - Artificial Intelligence
  - Reinforcement Learning
header:
  teaser: /assets/images/2023-04-17-reinforcement-learning-an-exploration/img01.png
  og_image: /assets/images/2023-04-17-reinforcement-learning-an-exploration/img01.png
---

{% raw %}


<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"  
  "http://www.w3.org/TR/html4/loose.dtd">  
<html > 
<head><title></title> 
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"> 
<meta name="generator" content="TeX4ht (https://tug.org/tex4ht/)"> 
<meta name="originator" content="TeX4ht (https://tug.org/tex4ht/)"> 
<!-- html --> 
<meta name="src" content="eloughlin3-analysis.tex"> 
<link rel="stylesheet" type="text/css" href="eloughlin3-analysis.css"> 
</head><body 
>
<!--l. 34--><p class="noindent" >
                                                                                                  
                                                                                                  
<!--l. 34--><p class="indent" >
                                                                                                  
                                                                                                  
<!--l. 34--><p class="noindent" ><span 
class="ptmr7t-x-x-240">Assignment 4: Markov Decision Processes</span>
<!--l. 34--><p class="noindent" >
<!--l. 34--><p class="noindent" >                                                                          <span 
class="ptmr7t-x-x-110">Evan Loughlin</span>
                                                              <span 
class="ptmr7t-x-x-110">CS7641: Machine Learning - Spring 2023</span>
                                                                      <span 
class="ptmr7t-x-x-110">eloughlin3@gatech.edu</span>
<!--l. 36--><p class="noindent" ><span 
class="ptmb7t-x-x-90">Index  Terms</span>
       <span 
class="ptmr7t-x-x-90">Machine Learning, Reinforcement Learning, Q Learning, Value Iteration, Policy Iteration</span>
<a 
 id="x1-2r1"></a>
<!--l. 43--><p class="noindent" ><span 
class="ptmrc7t-">I.  I<span 
class="small-caps">n</span><span 
class="small-caps">t</span><span 
class="small-caps">r</span><span 
class="small-caps">o</span><span 
class="small-caps">d</span><span 
class="small-caps">u</span><span 
class="small-caps">c</span><span 
class="small-caps">t</span><span 
class="small-caps">i</span><span 
class="small-caps">o</span><span 
class="small-caps">n</span></span>
<a 
 id="Q1-1-0"></a>
<!--l. 1--><p class="indent" >  Reinforcement learning is a sub-field of the overall machine learning field that focuses on algorithms that can learn from their local
environment through a process of trial and error interactions. These interactions involve an agent encountering a particular state, and
needing to decide on an action for that state. Rewards (or penalties) are computed based on the result of an action taken, which can
later contribute to the overall policy that is learned by the agent. <br 
class="newline" />
<!--l. 5--><p class="indent" >  In this report, reinforcement learning is studied experientially through a process of providing two well-known Markov-Decision
Process problems, and attempting to train agents to iteratively succeed in solving those problems. The algorithms are compared to one
another in terms of time, complexity, rewards versus iteration, and many other metrics. In particular, reinforcement learning algorithms
typically consist of hyperparameters which help tune the balance between exploration and exploitation, which is studied in depth.
<br 
class="newline" />
<!--l. 10--><p class="indent" >  Three reinforcement algorithms were applied in this study: Value Iteration, Policy Iteration, and Q-Learning.
<!--l. 46--><p class="indent" >
<a 
 id="x1-3r2"></a>
<!--l. 46--><p class="noindent" ><span 
class="ptmrc7t-">II.  M<span 
class="small-caps">a</span><span 
class="small-caps">r</span><span 
class="small-caps">k</span><span 
class="small-caps">o</span><span 
class="small-caps">v</span> D<span 
class="small-caps">e</span><span 
class="small-caps">c</span><span 
class="small-caps">i</span><span 
class="small-caps">s</span><span 
class="small-caps">i</span><span 
class="small-caps">o</span><span 
class="small-caps">n</span> P<span 
class="small-caps">r</span><span 
class="small-caps">o</span><span 
class="small-caps">c</span><span 
class="small-caps">e</span><span 
class="small-caps">s</span><span 
class="small-caps">s</span><span 
class="small-caps">e</span><span 
class="small-caps">s</span></span>
<a 
 id="Q1-1-0"></a>
<!--l. 2--><p class="indent" >  A Markov Decision Process is a framework that is frequently implemented in reinforcement learning. It&#8217;s used to model
decision-making problems, in particular those where outcomes of actions are often uncertain or stochastic in nature. <span class="cite">&#x00A0;[<a 
href="#Xbellman1957markovian">1</a>]</span> In the context
of this paper, the particular details of the MDP will be explained for the purpose of diving into each of the parameters for further
experimentation, study, and discussion.<br 
class="newline" />
    <ul class="itemize1">
    <li class="itemize">
    <!--l. 9--><p class="noindent" ><span 
class="cmsy-10"><img 
src="cmsy10-53.png" alt="S" class="10x-x-53" /> </span>is the state space, which is either finite or infinite, and is a set of possible states that the known environment can be
    in.
    </li>
    <li class="itemize">
    <!--l. 11--><p class="noindent" ><span 
class="cmsy-10"><img 
src="cmsy10-41.png" alt="A" class="10x-x-41" /> </span>is the action space, which is also either finite or infinite. It is set of possible actions that the agent can take under any
    circumstance.
    </li>
    <li class="itemize">
    <!--l. 12--><p class="noindent" ><span 
class="cmmi-10">P </span>is the transition function, which defines the probability of transitioning to a different state <span 
class="cmmi-10">s</span><span 
class="cmsy-10">&#x2032;</span>, given that the agent takes
    action <span 
class="cmmi-10">a </span>while in state <span 
class="cmmi-10">s</span>. The probability in this case can be described by <span 
class="cmmi-10">P</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s</span><span 
class="cmsy-10">&#x2032;|</span><span 
class="cmmi-10">s,a</span><span 
class="cmr-10">)</span>.
    </li>
    <li class="itemize">
    <!--l. 13--><p class="noindent" ><span 
class="cmmi-10">R </span>is the reward function, which is a map of each state-action pair to some reward value. The agent&#8217;s goal is to learn some
    policy whereby the expected cumulative reward over time is maximized. <span 
class="cmmi-10">R</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s,a</span><span 
class="cmr-10">) </span>describes the reward of taking action <span 
class="cmmi-10">a</span>
    while in state <span 
class="cmmi-10">s</span>.
    </li>
    <li class="itemize">
                                                                                                  
                                                                                                  
    <!--l. 14--><p class="noindent" ><span 
class="cmmi-10">&#x03B3; </span>(gamma) is the discount factor (between 0-1). This determines the value of future rewards, and can be understood by the
    adage &#8220;a dollar now is better than a dollar later&#8221;. How <span 
class="ptmri7t-">much </span>better is described by <span 
class="cmmi-10">&#x03B3;</span>. Formally, the expected cumulative
    reward at time <span 
class="cmmi-10">t </span>is given by <span 
class="cmmi-10">G</span><sub><span 
class="cmmi-7">t</span></sub> <span 
class="cmr-10">=</span> <span 
class="cmex-10">&#x2211;</span>
  <sub><span 
class="cmmi-7">k</span><span 
class="cmr-7">=0</span></sub><sup><span 
class="cmsy-7">&#x221E;</span></sup><span 
class="cmmi-10">&#x03B3;</span><sup><span 
class="cmmi-7">k</span></sup><span 
class="cmmi-10">R</span><sub><span 
class="cmmi-7">t</span><span 
class="cmr-7">+</span><span 
class="cmmi-7">k</span><span 
class="cmr-7">+1</span></sub>.</li></ul>
<!--l. 17--><p class="indent" >  With the above in mind, the MDP model captures the notion that environments (either open or closed) can be stochastic /
non-deterministic from the perspective of the agent. The agent&#8217;s actions can influence the probability of transitioning between states;
and ideally a good state. Given that our goal is for the agent to learn a policy which maximizes <span 
class="cmmi-10">G</span><sub><span 
class="cmmi-7">t</span></sub>, we achieve this by solving the
Bellman equations. The Bellman equations are an expression of the optimal value function <span 
class="cmmi-10">V</span> <sup><span 
class="cmsy-7">*</span></sup><span 
class="cmr-10">(</span><span 
class="cmmi-10">s</span><span 
class="cmr-10">)</span>, as well as the optimal action value
function <span 
class="cmmi-10">Q</span><sup><span 
class="cmsy-7">*</span></sup><span 
class="cmr-10">(</span><span 
class="cmmi-10">s,a</span><span 
class="cmr-10">)</span>.
    <ul class="itemize1">
    <li class="itemize">
    <!--l. 23--><p class="noindent" >The State-Value Function:
    <table 
class="equation-star"><tr><td>
<div class="math-display" >
<img 
src="eloughlin3-analysis0x.png" alt="V *(s) = max Q*(s,a) = max E[Gt |St = s,At = a]
        a&#x2208;A          a&#x2208;A
" class="math-display" ></div>
    </td></tr></table>
    <!--l. 25--><p class="nopar" >
    </li>
    <li class="itemize">
    <!--l. 27--><p class="noindent" >The Action-Value Function:
    <table 
class="equation-star"><tr><td>
<div class="math-display" >
<img 
src="eloughlin3-analysis1x.png" alt="  *                     *  &#x2032; &#x2032;
Q  (s,a) = E [Rt+1 + &#x03B3;maax&#x2032; Q (s,a )|St = s,At = a]
" class="math-display" ></div>
    </td></tr></table>
    <!--l. 29--><p class="nopar" ></li></ul>
<!--l. 49--><p class="indent" >
<a 
 id="x1-4r3"></a>
<!--l. 49--><p class="noindent" ><span 
class="ptmrc7t-">III.  A<span 
class="small-caps">l</span><span 
class="small-caps">g</span><span 
class="small-caps">o</span><span 
class="small-caps">r</span><span 
class="small-caps">i</span><span 
class="small-caps">t</span><span 
class="small-caps">h</span><span 
class="small-caps">m</span><span 
class="small-caps">s</span></span>
<a 
 id="Q1-1-0"></a>
<!--l. 1--><p class="indent" >
                                                                                                  
                                                                                                  
<a 
 id="x1-5r1"></a>
<!--l. 1--><p class="noindent" ><span 
class="ptmri7t-">A.  Value Iteration</span>
<a 
 id="Q1-1-0"></a>
<!--l. 2--><p class="indent" >  Value Iteration is a dynamic programming algorithm that works via iteratively updating the value function until
convergence happens. The value function <span 
class="cmmi-10">V </span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s</span><span 
class="cmr-10">) </span>is defined above and represents the expected total reward that an agent should
anticipate receiving from a particular state <span 
class="cmmi-10">s</span>, given the assumption that it continues to follow the optimal policy. The value
function can be thought of as a kind of &#8220;quality&#8221; or goodness metric for each state, thus allowing us to find the optimal
policy.
<!--l. 9--><p class="indent" >
<a 
 id="x1-6r2"></a>
<!--l. 9--><p class="noindent" ><span 
class="ptmri7t-">B.  Policy Iteration</span>
<a 
 id="Q1-1-0"></a>
<!--l. 10--><p class="indent" >  Policy Iteration is another algorithm, and is similar to Value Iteration; however instead of computing the optimal value function
directly, it works by iteratively improving some initial policy until that policy eventually converges to the optimal policy. This algorithm
is comprised of two primary steps:
    <ul class="itemize1">
    <li class="itemize">
    <!--l. 15--><p class="noindent" >Policy Evaluation: The value function is computed for a given policy (i.e. the total reward that can be obtained by following
    that policy). This is done by applying the Bellman equation in the form of <span 
class="cmmi-10">V </span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s</span><span 
class="cmr-10">) = </span><span 
class="cmmi-10">E</span><span 
class="cmr-10">[</span><span 
class="cmmi-10">r</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s,a</span><span 
class="cmr-10">)+</span><span 
class="cmmi-10">&#x03B3;</span><span 
class="cmsy-10">*</span><span 
class="cmmi-10">sum</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">p</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s</span><span 
class="cmsy-10">&#x2032;|</span><span 
class="cmmi-10">s,a</span><span 
class="cmr-10">)</span><span 
class="cmsy-10">*</span><span 
class="cmmi-10">V </span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s</span><span 
class="cmsy-10">&#x2032;</span><span 
class="cmr-10">))]</span>.
    This iteration continues until the value function converges.
    </li>
    <li class="itemize">
    <!--l. 16--><p class="noindent" >Policy  Improvement:  Once  we  have  the  value  function,  we  can  improve  the  policy  by  choosing  actions  whereby
    the  expected  total  reward  is  maximized  from  each  state  <span 
class="cmmi-10">s</span>.  This  update  occurs  in  the  following  form:  <span 
class="cmmi-10">pi</span><span 
class="cmsy-10">&#x2032;</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s</span><span 
class="cmr-10">)  =</span>
    <span 
class="cmmi-10">argmax</span><span 
class="cmr-10">[</span><span 
class="cmmi-10">a</span><span 
class="cmr-10">]</span><span 
class="cmmi-10">r</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s,a</span><span 
class="cmr-10">) + </span><span 
class="cmmi-10">&#x03B3; </span><span 
class="cmsy-10">* </span><span 
class="cmmi-10">sum</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">p</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s</span><span 
class="cmsy-10">&#x2032;|</span><span 
class="cmmi-10">s,a</span><span 
class="cmr-10">) </span><span 
class="cmsy-10">* </span><span 
class="cmmi-10">V </span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s</span><span 
class="cmsy-10">&#x2032;</span><span 
class="cmr-10">))</span>.</li></ul>
<!--l. 19--><p class="indent" >
<a 
 id="x1-7r3"></a>
<!--l. 19--><p class="noindent" ><span 
class="ptmri7t-">C.  Q Learning</span>
<a 
 id="Q1-1-0"></a>
<!--l. 20--><p class="indent" >  Q-Learning is a model-free reinforcement learning algorithm. In the case of Q-Learning, the algorithm learns Q-Values for the
optimal policy even if it is not following that policy during the learning process. <span class="cite">&#x00A0;[<a 
href="#XWatkins1992">6</a>]</span>
<!--l. 23--><p class="indent" >  Q-Learning works to find the optimal policy in an MDP by learning an action-value function, <span 
class="cmmi-10">Q</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s,a</span><span 
class="cmr-10">)</span>. This action-value function
tries to estimate the expected discounted cumulative reward when the agent completes action <span 
class="cmmi-10">a </span>in state <span 
class="cmmi-10">s</span>, assuming that it continues to
follow the known optimal policy thereafter. This is updated iteratively as the agent learns through episodes of interaction with its
environment <span 
class="msbm-10">E</span>.
<!--l. 28--><p class="indent" >  The algorithm first initializes <span 
class="cmmi-10">Q</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s,a</span><span 
class="cmr-10">) </span>(all the Q-Values), after which, at each time step <span 
class="cmmi-10">t</span>, the agent observes the
current state <span 
class="cmmi-10">s</span><sub><span 
class="cmmi-7">t</span></sub>, then selects an action <span 
class="cmmi-10">a</span><sub><span 
class="cmmi-7">t</span></sub> based on its current exploration-exploitation configuration (a strategy that is
implemented here is epsilon-greedy). It then can gain a reward (or penalty) <span 
class="cmmi-10">r</span><sub><span 
class="cmmi-7">t</span></sub> while also observing the new state that
it  arrived  in,  <span 
class="cmmi-10">s</span><span 
class="cmsy-10">&#x2032; </span>at  <span 
class="cmmi-10">t </span><span 
class="cmr-10">+ 1</span>.  From  this  information,  it  can  update  its  Q-Value  for  that  current  state  <span 
class="cmmi-10">s </span>and  action  <span 
class="cmmi-10">a</span>,  as
follows:
    <ul class="itemize1">
    <li class="itemize">
    <!--l. 34--><p class="noindent" ><span 
class="cmmi-10">Q</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s</span><sub><span 
class="cmmi-7">t</span></sub><span 
class="cmmi-10">,a</span><sub><span 
class="cmmi-7">t</span></sub><span 
class="cmr-10">) = </span><span 
class="cmmi-10">Q</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s</span><sub><span 
class="cmmi-7">t</span></sub><span 
class="cmmi-10">,a</span><sub><span 
class="cmmi-7">t</span></sub><span 
class="cmr-10">) + </span><span 
class="cmmi-10">alpha </span><span 
class="cmsy-10">* </span><span 
class="cmr-10">[</span><span 
class="cmmi-10">r</span><sub><span 
class="cmmi-7">t</span></sub> <span 
class="cmr-10">+ </span><span 
class="cmmi-10">gamma </span><span 
class="cmsy-10">* </span><span 
class="cmmi-10">max</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">Q</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s</span><sub><span 
class="cmmi-7">t</span><span 
class="cmr-7">+1</span></sub><span 
class="cmmi-10">,a</span><span 
class="cmr-10">)) </span><span 
class="cmsy-10">- </span><span 
class="cmmi-10">Q</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s</span><sub><span 
class="cmmi-7">t</span></sub><span 
class="cmmi-10">,a</span><sub><span 
class="cmmi-7">t</span></sub><span 
class="cmr-10">)]</span></li></ul>
<!--l. 37--><p class="indent" >  In the above equation, alpha refers to the learning rate, and gamma is the discount factor discussed previously. The value
<span 
class="cmmi-10">max</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">Q</span><span 
class="cmr-10">(</span><span 
class="cmmi-10">s</span><sub><span 
class="cmmi-7">t</span><span 
class="cmr-7">+1</span></sub><span 
class="cmmi-10">,a</span><span 
class="cmr-10">)) </span>refers to the maximum Q-Value over all possible action-state pairs in the upcoming state <span 
class="cmmi-10">s</span><span 
class="cmsy-10">&#x2032;</span>. These Q-Values
iteratively update, such that the agent learns which actions are favorable in a given state. In the case of this report, the exploration
strategy of Epsilon-Greedy was used, and epsilon was tweaked.
<!--l. 52--><p class="indent" >
<a 
 id="x1-8r4"></a>
<!--l. 52--><p class="noindent" ><span 
class="ptmrc7t-">IV.  P<span 
class="small-caps">r</span><span 
class="small-caps">o</span><span 
class="small-caps">b</span><span 
class="small-caps">l</span><span 
class="small-caps">e</span><span 
class="small-caps">m</span><span 
class="small-caps">s</span></span>
<a 
 id="Q1-1-0"></a>
<!--l. 1--><p class="indent" >
                                                                                                  
                                                                                                  
<a 
 id="x1-9r1"></a>
<!--l. 1--><p class="noindent" ><span 
class="ptmri7t-">A.  MDP I: Frozen World</span>
<a 
 id="Q1-1-0"></a>
<!--l. 2--><p class="indent" >  The Frozen World problem <span class="cite">&#x00A0;[<a 
href="#X1606.01540">3</a>]</span> was selected as the first example to study. In this problem, the agent is situated in a grid-world made
up of cells. The world is presumably a frozen lake, whereby many holes exist that the agent could slip and fall into. The
agents&#8217; falling into a hole would result in a penalty, as defined by the reward function. The goal of the agent is to
navigate the lake, avoiding holes, and eventually retrieving the goal (a package on the bottom-right of each map). The
interesting component of this problem is the stochastic nature of it. Since the lake is considered icy / slippery, for each
action <span 
class="cmmi-10">a </span>that is attempted to be taken by the agent, there is a probability of <span 
class="cmr-10">1</span><span 
class="cmmi-10">&#x2215;</span><span 
class="cmr-10">3 </span>that the agent moves in a different
direction altogether. This makes policy finding less simple than, say, determining the shortest path with an algorithm
such  as  <span 
class="cmmi-10">A</span><sup><span 
class="cmsy-7">*</span></sup> <span class="cite">&#x00A0;[<a 
href="#Xhart1968formal">4</a>]</span>.  The  reward  function  <span 
class="cmmi-10">R </span>for  this  problem  is  defined  such  that  each  step  in  the  frozen  world  costs
<span 
class="cmsy-10">-</span><span 
class="cmr-10">0</span><span 
class="cmmi-10">.</span><span 
class="cmr-10">1</span>, falling into a hole costs <span 
class="cmsy-10">-</span><span 
class="cmr-10">100</span>, and getting to the goal state awards <span 
class="cmr-10">+1000</span>. Due to the stochastic nature the
transition function, the learned policy needs to reflect the rewards not just of the next state, but of future states from
making a given decision. Such stochastic nature forces that the agent learn a more robust policy that can handle the
uncertainty in the environment. This provides an opportunity to study how different RL algorithms perform in stochastic
domains.
<!--l. 17--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/frozen_small.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-10r1"></a>
                                       <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;1.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;Frozen World - Small</span>
                                                                                                  
                                                                                                  
<!--l. 22--><p class="indent" >  </div><hr class="endfigure">
<!--l. 24--><p class="indent" >  In order to experiment with the effect of state size on the performance of each of the algorithms, three versions of the Frozen World
problem were implemented. The first, &#8220;Small&#8221; problem is a 4x4 grid, totaling a state space <span 
class="cmsy-10"><img 
src="cmsy10-53.png" alt="S" class="10x-x-53" /> </span>of 16 possible states (Fig
<a 
href="#x1-10r1">1<!--tex4ht:ref: g0 --></a>).
<!--l. 28--><p class="indent" >  The second, &#8220;Medium&#8221; problem generated is a 12x12 grid, and has a state space <span 
class="cmsy-10"><img 
src="cmsy10-53.png" alt="S" class="10x-x-53" /> </span>consisting of 144 possible states. In each of the
problems, the action space <span 
class="cmsy-10"><img 
src="cmsy10-41.png" alt="A" class="10x-x-41" /> </span>is defined by the set of movements: <span 
class="cmmi-10">Up,Down,Left,Right</span>.
<!--l. 31--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/frozen_large.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-11r2"></a>
                                       <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;2.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;Frozen World - Large</span>
                                                                                                  
                                                                                                  
<!--l. 36--><p class="indent" >  </div><hr class="endfigure">
<!--l. 38--><p class="indent" >  The third, &#8220;Large&#8221; problem generated is a 40x40 grid, and therefore has a state space up to 1600 possible states to explore (Fig <a 
href="#x1-11r2">2<!--tex4ht:ref: g2 --></a>).
<br 
class="newline" />
<!--l. 40--><p class="indent" >  Given the descriptions of how each of the algorithms work, as well as the definition of the Frozen Lake problem, several hypotheses
can be made that will be explored in more depth:
     <ol  class="enumerate1" >
<li 
  class="enumerate" id="x1-13x1">
     <!--l. 44--><p class="noindent" >Value  Iteration  might  tend  to  converge  more  quickly  (in  wall  clock  time)  than  does  Policy  Iteration  and  Q-Learning,
     since the value function in each iteration gets updated, and it uses a greedy policy which should be suitable for such a
     grid-world problem.
     </li>
<li 
  class="enumerate" id="x1-15x2">
     <!--l. 45--><p class="noindent" >Policy iteration should require fewer iterations than either Value Iteration or Q-Learning. This is because the algorithm
     is  more  computation-intensive  early  on,  since  it  alternates  between  policy  evaluation  and  policy  improvement  steps,
     allowing it to converge in fewer steps.
     </li>
<li 
  class="enumerate" id="x1-17x3">
     <!--l. 46--><p class="noindent" >Q-Learning might be more robust at solving the stochastic nature (slippery) of the Frozen World problem, since it learns
     an optimal policy via trial-and-error rather than through pre-planning of policies.</li></ol>
<!--l. 49--><p class="indent" >  Of course, more findings will be discussed as they arise through the experimentation process.
<a 
 id="x1-18r2"></a>
<!--l. 51--><p class="noindent" ><span 
class="ptmri7t-">B.  MDP II: Taxi Problem</span>
<a 
 id="Q1-1-2"></a>
<!--l. 53--><p class="indent" >  The Taxi Problem is another useful classic reinforcement learning problem, which involves a Taxi navigating through a grid-world to
pick up and drop off passengers at specific locations. It differs fundamentally from the Frozen World problem in several ways. Notably,
there is less of a stochastic nature in the transition function. Whereas in the Frozen World problem, the slippery nature resulted in a <span 
class="cmr-10">1</span><span 
class="cmmi-10">&#x2215;</span><span 
class="cmr-10">3</span>
chance of moving to a random nearby state, the Taxi problem has a <span 
class="cmr-10">1</span><span 
class="cmmi-10">&#x2215;</span><span 
class="cmr-10">10 </span>probability of the same. More importantly, however, is the
difference that the Taxi problem has a multi-staged set of goals. While it does not have a passenger, it must look for
a nearby passenger, and then deliver that passenger to their preferred destination. This elicits interesting behaviour
that RL algorithms often face in more complex domains. The multi-step sequence of actions to achieve a goal can
cause a sparse reward structure that makes it difficult for some algorithms to learn an optimal policy. Refer to Figure
<a 
href="#x1-19r3">3<!--tex4ht:ref: fhvxsc --></a>.
<!--l. 65--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/taxi-world.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-19r3"></a>
                                           <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;3.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;Taxi World</span>
                                                                                                  
                                                                                                  
<!--l. 70--><p class="indent" >  </div><hr class="endfigure">
<!--l. 72--><p class="indent" >  In the implemented problem, there are 4 possible locations, a single taxi, and a single passenger. The taxi, destination, and passenger
can each spawn at a random location (one of four) for each environment reset. The state space <span 
class="cmsy-10"><img 
src="cmsy10-53.png" alt="S" class="10x-x-53" /> </span>is defined by the number of possible
states the environment can be in. In this case, the grid is 5x5, so there are 25 cells. The passenger can be in one of four locations, as
well as inside the taxi, and the destination can be in one of four locations. Therefore, the <span 
class="cmsy-10">|<img 
src="cmsy10-53.png" alt="S" class="10x-x-53" />| </span><span 
class="cmr-10">= 25 </span><span 
class="cmsy-10">* </span><span 
class="cmr-10">5 </span><span 
class="cmsy-10">* </span><span 
class="cmr-10">4 = 500</span>. The action space <span 
class="cmsy-10"><img 
src="cmsy10-41.png" alt="A" class="10x-x-41" /></span>
can be defined by the following set: <span 
class="cmmi-10">Up,Down,Left,Right,PickUp,DropOff</span>. The rewards of the taxi problem are
defined as follows: (-1 for each action taken by the taxi, -10 for an unsuccessful drop-off, and +20 for a successful
drop-off).
<!--l. 79--><p class="indent" >  Some hypotheses can be made regarding how the algorithms might perform:
     <ol  class="enumerate1" >
<li 
  class="enumerate" id="x1-21x1">
     <!--l. 82--><p class="noindent" >The Q-Learning algorithm, since it is off-policy, will likely perform well on this problem, since the Taxi Problem involves
     a discrete action and state space. However, it will take longer to converge to the optimal policy than Value Iteration and
     Policy Iteration.
     </li>
<li 
  class="enumerate" id="x1-23x2">
     <!--l. 83--><p class="noindent" >The Q-Learning algorithm will be sensitive to the exploration / exploitation hyperparameters, but tuning them will help
     the problem become more robust against falling into suboptimal policies
     </li>
<li 
  class="enumerate" id="x1-25x3">
     <!--l. 84--><p class="noindent" >The  Value  Iteration  algorithm  will  perform  well  on  the  Taxi  problem  because  the  state  space  is  relatively  small  (500
     states).  However,  since  the  Taxi  problem  involves  key  features  of  exploration  /  exploitation  due  to  its  multi-sequence
     reward structure, Value Iteration may get stuck in a suboptimal policy.
     </li>
<li 
  class="enumerate" id="x1-27x4">
     <!--l. 85--><p class="noindent" >The Policy Iteration algorithm will similarly perform well on the Taxi problem due to its small state space, however it&#8217;s
     possible that if the state space is not explored effectively, it can similarly get stuck in a suboptimal policy.</li></ol>
<a 
 id="x1-28r5"></a>
<!--l. 55--><p class="noindent" ><span 
class="ptmrc7t-">V.  E<span 
class="small-caps">x</span><span 
class="small-caps">p</span><span 
class="small-caps">e</span><span 
class="small-caps">r</span><span 
class="small-caps">i</span><span 
class="small-caps">m</span><span 
class="small-caps">e</span><span 
class="small-caps">n</span><span 
class="small-caps">t</span><span 
class="small-caps">a</span><span 
class="small-caps">t</span><span 
class="small-caps">i</span><span 
class="small-caps">o</span><span 
class="small-caps">n</span>: F<span 
class="small-caps">r</span><span 
class="small-caps">o</span><span 
class="small-caps">z</span><span 
class="small-caps">e</span><span 
class="small-caps">n</span> W<span 
class="small-caps">o</span><span 
class="small-caps">r</span><span 
class="small-caps">l</span><span 
class="small-caps">d</span></span>
<a 
 id="Q1-1-3"></a>
<!--l. 2--><p class="indent" >
<a 
 id="x1-29r1"></a>
<!--l. 2--><p class="noindent" ><span 
class="ptmri7t-">A.  Value Iteration</span>
<a 
 id="Q1-1-3"></a>
<!--l. 4--><p class="indent" >  The Value Iteration algorithm was applied to each size of the Frozen World problem, and many interesting analytics were gathered.
Notably, Value Heatmaps were generated for varying values of gamma, in order to study how the effect of discounting future rewards
can impact the overall policy. It&#8217;s important to note that although these are being called Policy Heatmaps, they&#8217;re in fact heatmaps of
the value function <span 
class="cmmi-10">V  </span>for each state. Given that the action space of the Frozen World problem is a simple space of 4
movements, it&#8217;s easy to recognize the policy that is chosen from each would align with the movement within areas of high
reward.
<!--l. 12--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Policy Heatmap - FrozenLake40x40-v1 - Value Iteration - gamma=0.5.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-30r4"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;4.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 17--><p class="indent" >  </div><hr class="endfigure">
<!--l. 19--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Policy Heatmap - FrozenLake40x40-v1 - Value Iteration - gamma=0.99.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-31r5"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;5.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 24--><p class="indent" >  </div><hr class="endfigure">
<!--l. 26--><p class="indent" >  Comparing figures <a 
href="#x1-30r4">4<!--tex4ht:ref: vhjmgt --></a> and <a 
href="#x1-31r5">5<!--tex4ht:ref: hykizy --></a>, a very interesting visual representation of the effects of gamma on the value function <span 
class="cmmi-10">V </span>and
the overall policies selected can be seen. When gamma is low, most of the states are considered to have much more
similar ranges of value. This means that there&#8217;s less likelihood that the policy would attempt to avoid potential hazards.
When the gamma is set to be high, a clear distinction between safe states and unsafe states is made, whereby the
agent is more likely to favor avoiding states which might cause it to fall into a hole. This is intuitive, since a low
gamma means that future rewards are given less weight, and only immediate rewards are considered. Therefore, for
larger state spaces, a low gamma might have the effect of causing the <span 
class="cmmi-10">V </span>to not propagate back from a far-away goal
state.
<!--l. 33--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Reward vs Iteration - Varying Gamma - FrozenLake40x40-v1 - Value Iteration.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-32r6"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;6.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 38--><p class="indent" >  </div><hr class="endfigure">
<!--l. 40--><p class="indent" >  Figure <a 
href="#x1-32r6">6<!--tex4ht:ref: mvftxn --></a> also captures this trend, where the greatest reward tends to be found when the discount factor is highest. In environments
with high uncertainty, low gamma can help the agent focus on the present and near future. However, in the Frozen World example, the
goal state is far away, and therefore it&#8217;s critical to find the end state. A low gamma might help the agent avoid nearby holes, however
might cause difficult in finding a policy that navigates to the goal. The Value Iteration seems to have converged on suboptimal policies
when the gamma is set too low.
<!--l. 45--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Error vs Iteration - Varying Gamma - FrozenLake40x40-v1 - Value Iteration.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-33r7"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;7.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 50--><p class="indent" >  </div><hr class="endfigure">
<!--l. 52--><p class="indent" >  Figure <a 
href="#x1-33r7">7<!--tex4ht:ref: lcfhib --></a> shows how error changes by iteration, and is helpful to see since it correlates with the rate at which convergence occurs,
showing how policies that were overall unable to find the end goal would converge more quickly since they tended to frequently fail to
find the objective.
<!--l. 55--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Reward vs Iteration - All Sizes - Frozen World - Value Iteration - gamma=0.99 - epsilon=0.05.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-34r8"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;8.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 60--><p class="indent" >  </div><hr class="endfigure">
<!--l. 62--><p class="indent" >  Reviewing Figure <a 
href="#x1-34r8">8<!--tex4ht:ref: eaburx --></a> shows a comparison between the the reward versus iteration curves (learning curves) for each of the 4 sizes of
the Frozen World problem studied. Note however that higher reward doesn&#8217;t necessarily correlate entirely to better performance in this
comparison, since larger problems will naturally incur larger decreases per time-step (while moving on Frozen earth), therefore the total
rewards are not entirely comparable. What is interesting, however, is perhaps the proportion of times that an agent was or was not
successful in reaching its destination.
<!--l. 69--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Time vs Iteration - All Sizes - Frozen World - Value Iteration - gamma=0.99 - epsilon=0.05.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-35r9"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;9.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 74--><p class="indent" >  </div><hr class="endfigure">
<!--l. 76--><p class="indent" >  Figure <a 
href="#x1-35r9">9<!--tex4ht:ref: yodesi --></a> shows how the time complexity relates to the size of the state space, which is known to be <span 
class="cmmi-10">O</span><span 
class="cmr-10">(</span><span 
class="cmsy-10">|<img 
src="cmsy10-53.png" alt="S" class="10x-x-53" />|</span><sup><span 
class="cmr-7">2</span></sup><span 
class="cmsy-10"><img 
src="cmsy10-41.png" alt="A" class="10x-x-41" /></span><span 
class="cmr-10">) </span><span class="cite">
&#x00A0;[<a 
href="#Xsutton2018reinforcement">5</a>]</span>. It is notable that although the &#8220;large&#8221; Frozen World problem is studied here, 1600 states is actually quite small,
relatively. Due to this, the Value Iteration algorithm did appear to succeed quite well; particularly since grid-world
problems like Frozen World are particularly well suited to such planner alorithms because the state of the environment is
known in its entirety. This will be discussed further, and in particular contrasted to the strengths of the Q-Learning
algorithm.
<a 
 id="x1-36r2"></a>
<!--l. 82--><p class="noindent" ><span 
class="ptmri7t-">B.  Policy Iteration</span>
<a 
 id="Q1-1-9"></a>
<!--l. 84--><p class="indent" >  Interestingly, the Value Maps for the varying of gamma for Policy Iteration preformed essentially the same as in Value Iteration
(Figures not included for brevity, but they appear nearly the same). This can be further explored in the Reward versus Iteration graph,
comparing varying levels of gamma for the Policy Iteration algorithm. Although 1000 episodes were run, the convergence occured
relatively quickly in all cases. Within the first 4 or 5 iterations. However, the total average rewards determined by the chosen policies
remained static, where the highest reward was obtained again with the highest available gamma. This further reinforces the argument
that for relatively larger state spaces, the benefit of considering far-in future rewards (with high gamma) pays off in the success of the
learned policy.
<!--l. 92--><p class="indent" >  The reward versus iteration learning curve for different values of gamma is shown in Figure <a 
href="#x1-37r10">10<!--tex4ht:ref: fwzwmc --></a>. The most obvious thing to
notice about the graphs generated for Policy Iteration is how they compare, in terms of convergence rate, to the Value
Iteration graphs. The difference between the algorithms lays in that Policy Iteration combines both the policy evaluation
and policy improvement steps. This means that at each iteration, policy iteration is a more computationally intensive
algorithm.
<!--l. 99--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Reward vs Iteration - Varying Gamma - FrozenLake40x40-v1 - Policy Iteration.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-37r10"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;10.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 104--><p class="indent" >  </div><hr class="endfigure">
<!--l. 106--><p class="indent" >  The shape of the learning curves can be explained by how these algorithms differ from one another.
<!--l. 108--><p class="indent" >  In Policy Iteration, the policy can jump to a much better solution quickly once it lands upon a better set of actions for each state. As
a result, the learning curve is likely shooting vertically up in the initial stages of the algorithm; especially since the initial policy is
poor.
<!--l. 115--><p class="indent" >  In contrast, Value Iteration iteratively updates the policy at the end of each iteration. This generally means that the policy can
improve gradually as the value estimates become more accurate, resulting in a smoother curve-looking increase in the reward over time
/ per iteration.
<!--l. 120--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Reward vs Iteration - All Sizes - Frozen World - Policy Iteration - gamma=0.99 - epsilon=0.05.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-38r11"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;11.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 125--><p class="indent" >  </div><hr class="endfigure">
<a 
 id="x1-39r3"></a>
<!--l. 128--><p class="noindent" ><span 
class="ptmri7t-">C.  Q Learning</span>
<a 
 id="Q1-1-11"></a>
<!--l. 130--><p class="indent" >  Overall, the Q-Learning algorithm showed very interesting results in how it behaved against the Frozen World problem. This was an
interesting algorithm to apply because of how important hyperparameter tuning is for it; particularly in the sense of exploration versus
exploitation trade-off. The graphs provided in no way imply that the Q-Learning algorithm is unsuitable for or incapable of solving the
problems it was applied to. Rather, the results provided were done so intentionally to describe the effects that particular
hyperparameters have on the overall performance of the algorithm.
<!--l. 137--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Reward vs Iteration - All Sizes - Frozen World - Q Learning - gamma=0.99 - epsilon=0.05.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-40r12"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;12.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 142--><p class="indent" >  </div><hr class="endfigure">
<!--l. 144--><p class="indent" >  It is immediately obvious that while the policy iteration and value iteration algorithms show relatively smooth or straight lines for
reward, the Q-Learning algorithm jitters dramatically, oscillating with a large degree of randomness. In fact, the oscillating effect is
even greater than displayed, since the output shown displays values of moving averages of the reward values. This difference is
expected, and demonstrates fundamental differences between the algorithms. Both policy and value iteration algorithms rely on models,
and have a full view of the environment. They also must know the transition probabilities, and therefore have the capability of
computing the average value of each state in the state space, given its probability of reaching the goal state. For this reason, when the
total reward is computed, it&#8217;s computed based upon its own internal policy. In contrast, the Q-Learning algorithm is
model-free, and therefore does not have a way to pre-plan or pre-compute its optimal policy. It therefore relies on
experience, and since that experience is inherently stochastic, there will be times where, when following its own known best
policies for given states, it will fail and fall into a bad state. The algorithm relies on such failures (or successes) to
continuously update its Q values, thus learning from experience, rather than knowledge of a model, to improve its
performance.
<!--l. 155--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Policy Heatmap - FrozenLake40x40-v1 - Q Learning - epsilon=0.05 - gamma=0.99.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-41r13"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;13.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 160--><p class="indent" >  </div><hr class="endfigure">
<!--l. 162--><p class="indent" >  Looking at Figure <a 
href="#x1-40r12">12<!--tex4ht:ref: bjufgl --></a> shows the various performances of Q-Learning in the various sizes of the Frozen World problem. This graph
depicts interesting features; that although the algorithm found some success in smaller state spaces, when the state space became large
enough, it failed to converge upon any success of finding the reward. There are many possible reasons for this that will be discussed. A
review of Figure <a 
href="#x1-41r13">13<!--tex4ht:ref: lchwlw --></a> is revealing in this regard. In contrast to the Value Iteration and Policy Iteration algorithm where the value
heatmap was capable of more-or-less depicting the entire state space (including dangers and rewards), the Q-Learning
algorithm demonstrates that, aside from negative states (holes) near the start state, the large majority of the southern
territories remained unexplored. This may be explanatory as to why the Q-Learning algorithm failed to converge in these
cases.
<!--l. 169--><p class="indent" >  Epsilon was tuned, and analysed. Epsilon controls the rate at which the agent will take random actions despite its
known policies. With higher rates of exploration, the agent increases its chances of visiting new states that it hasn&#8217;t
previously explored. However, it also increases the chances that the agent falls into a hole. However, if remaining on frozen
tundra has a negative consequence, this too might play into the performance of the Q-Learning algorithm. The agent
might &#8220;realize&#8221; that due to the stochastic nature of the problem and the low likelihood of finding the reward through
random exploration, it&#8217;s simply better to immediately jump into a hole as soon as possible (fast death is better than
slow death). In the tuning of epsilon, it can be seen that lower values of epsilon initially have higher rates of success,
however as iterations proceed, they all converge upon the same rate of success. This might be explained by the fact
that, with a low epsilon, the agent explores less and is therefore more capable during early iterations to learn which
areas to avoid, whereas with high epsilon, early iterations might make far more mistakes but learn from them more
quickly.
<!--l. 179--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Error vs Iteration - Varying Epsilon - FrozenLake40x40-v1 - Q Learning - gamma = 0.99.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-42r14"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;14.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 184--><p class="indent" >  </div><hr class="endfigure">
<!--l. 186--><p class="indent" >  This hypothesis is supported also by Figure <a 
href="#x1-42r14">14<!--tex4ht:ref: usnixt --></a> which demonstrates that the rate of error tends to start low for low values of epsilon
(low exploration), but eventually appears to match (with enough iterations) the rate of error that is seen with higher values of epsilon;
as those competing versions of the algorithm eventually learn better policies. Additionally, it must be noted that the version of
Q-Learning implemented has a notion of epsilon decay. That is, as iterations progress, the epsilon value slowly decreases. This helps
the algorithm to gain large amounts of experience about broad areas of the state space relatively quickly, but then to eventually utilize
that experience more maturely and form policies that help it learn perform at a high enough level. This type of epsilon-decay behaviour
is interestingly seen in nature; particularly in humans where young adults tend to be less risk averse to the world and more apt
to explore new ideas not taught to them by their elders; however as they age and grow, tend to settle into patterns
that have kept them comfortable. This concept is also analogous to white matter in brains and the concept of brain
elasticity.
<!--l. 195--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Error vs Iteration - Varying Gamma - FrozenLake40x40-v1 - Q Learning - epsilon = 0.95.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-43r15"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;15.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 200--><p class="indent" >  </div><hr class="endfigure">
<!--l. 202--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Time vs Iteration - All Sizes - Frozen World - Q Learning - gamma=0.99 - epsilon=0.05.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-44r16"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;16.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 207--><p class="indent" >  </div><hr class="endfigure">
<!--l. 209--><p class="indent" >  The timing curve of the Q-Learning algorithm for varying sizes of the Frozen World problem is depicted in Figure <a 
href="#x1-44r16">16<!--tex4ht:ref: ombjfb --></a>, and it&#8217;s clear
to see that greater state sizes do correspond with greater time required per iteration.
<a 
 id="x1-45r4"></a>
<!--l. 213--><p class="noindent" ><span 
class="ptmri7t-">D.  Algorithm Overall Comparison</span>
<a 
 id="Q1-1-16"></a>
<!--l. 215--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Time vs Iteration - All Algorithms- FrozenLake40x40-v1 - gamma=0.99.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-46r17"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;17.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 220--><p class="indent" >  </div><hr class="endfigure">
<!--l. 222--><p class="indent" >  A certain impression might be unintentionally left by the results being sub-par for the Q-Learning algorithm, giving it unfair
representation. For almost every metric studied, the Q-Learning algorithm performed worse. It&#8217;s therefore suitable to mention that grid
world problems like the Frozen World problem are particularly well suited for planner algorithms like Value / Policy Iteration. However,
such example is a toy problem and has considerable simplifications that need to be understood. Most importantly, both VI and PI know
about the transition probabilities; they have pre-built models that are directly aware of the probabilities by which an agent would &#8220;slip&#8221;
on ice. How realistic of a problem is this? Not very. In reality, probability functions for transitions are extremely difficult to
predict or know before-hand. This is where Q-Learning algorithms can excel, since it can take advantage of repeated
iterations of experience, exploration, and exploitation to learn about its environment without needing any sort of model.
This  lack  of  built-in  model  regarding  the  local  environment  might  be  considered  closer  to  reality  for  many  useful
cases.
<a 
 id="x1-47r6"></a>
<!--l. 58--><p class="noindent" ><span 
class="ptmrc7t-">VI.  E<span 
class="small-caps">x</span><span 
class="small-caps">p</span><span 
class="small-caps">e</span><span 
class="small-caps">r</span><span 
class="small-caps">i</span><span 
class="small-caps">m</span><span 
class="small-caps">e</span><span 
class="small-caps">n</span><span 
class="small-caps">t</span><span 
class="small-caps">a</span><span 
class="small-caps">t</span><span 
class="small-caps">i</span><span 
class="small-caps">o</span><span 
class="small-caps">n</span>: T<span 
class="small-caps">a</span><span 
class="small-caps">x</span><span 
class="small-caps">i</span></span>
<a 
 id="Q1-1-17"></a>
<!--l. 2--><p class="indent" >
<a 
 id="x1-48r1"></a>
<!--l. 2--><p class="noindent" ><span 
class="ptmri7t-">A.  Value Iteration</span>
<a 
 id="Q1-1-17"></a>
<!--l. 4--><p class="indent" >  Given that a considerable amount of time has been spent already discussing the behaviour of algorithms on the Frozen World
problem, this analysis and experimentation will focus primarily on how the problem differs, as well as upon hypothesizing the pros and
cons of each of the algorithms with which the problem was solved.
<!--l. 8--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Error vs Iteration - Varying Gamma - Taxi-v3 - Value Iteration.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-49r18"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;18.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 13--><p class="indent" >  </div><hr class="endfigure">
<!--l. 15--><p class="indent" >  The Value Iteration and Policy Iteration algorithms are known to be excellent for relatively small state spaces, but can frequently
suffer when the state size or complexity becomes great <span class="cite">&#x00A0;[<a 
href="#XBertsekas:1996:NNL:560962">2</a>]</span>. In terms of the Taxi problem presented, both algorithms made short work
of them in terms of converging to acceptably high rewards. However, it should be noted that the Taxi problem presented was relatively
small. A much greater problem size could be introduced by, for example, increasing the number of cells in the grid, increasing the
number of passengers, increasing the number of possible locations, and maybe even introducing competing taxis with varying
fares. In this expanded example, both the state size and the action space increases, greatly increasing the size of the
problem. When such a problem size increases like this, the memory and time required to maintain a model of the
environment can become exhaustive and prohibitive, in which case a model-free algorithm such as Q-Learning might be
preferred.
<!--l. 24--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Reward vs Iteration - Varying Gamma - Taxi-v3 - Value Iteration.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-50r19"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;19.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 29--><p class="indent" >  </div><hr class="endfigure">
<!--l. 31--><p class="indent" >  The first graph to consider is Figure <a 
href="#x1-49r18">18<!--tex4ht:ref: udnzkm --></a>, whereby the convergence rate can be intuited from the rate at which error falls with
variations in the gamma rate. Additionally, reviewing Figure <a 
href="#x1-50r19">19<!--tex4ht:ref: nhhfve --></a>, it&#8217;s clear to see that if the discount rate is too low, future rewards
cannot be intuited and propagated back to the policy, which can be noticed when considering that the algorithm tended to converge to
suboptimal policies with suboptimal reward structures. This supports the argument just made that Value Iteration and Policy Iteration
might struggle to continuously improve and learn from ongoing experience when the size of the problem becomes difficult to
compute.
<!--l. 38--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Time vs Iteration - All Algorithms- Taxi-v3 - gamma=0.99.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-51r20"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;20.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 43--><p class="indent" >  </div><hr class="endfigure">
<!--l. 45--><p class="indent" >  In contrast, the Q-Learning algorithm is model-free and can handle larger state spaces more effectively, although it might take much
longer and many more iterations with an effective exploration parameters tuned to gain this benefit. The comparative time sequences
can be seen in Figure <a 
href="#x1-51r20">20<!--tex4ht:ref: lchbac --></a>. It can be seen that although Policy Iteration required more time per iteration, it &#8220;solved&#8221; the model with
very few iterations. This is similar to Value Iteration, although value iteration managed to converge after many more
iterations. In contrast, the Q-Learning algorithm took a very large number of iterations, and did not terminate based
on some reduction in error. As previously discussed, the jittery nature of the Q-Learning reward graph is also seen
here.
<!--l. 51--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Reward vs Iteration - All Algorithms- Taxi-v3 - gamma=0.99.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-52r21"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;21.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 56--><p class="indent" >  </div><hr class="endfigure">
<!--l. 58--><p class="indent" >  Figure <a 
href="#x1-52r21">21<!--tex4ht:ref: shxotf --></a> shows the Reward versus Iteration, comparing each of the algorithms studied. It&#8217;s important to note that in this graph, the
rewards were computed slightly differently for the purposes of displaying the algorithms, Whereas the Q-Learning algorithm appears to
have converged upon zero reward, it in fact performed with a similar degree of success as both the Value Iteration and
Policy Iteration algorithms. A successful policy was found in all three cases, although clearly in following different
methodologies.
<a 
 id="x1-53r2"></a>
<!--l. 63--><p class="noindent" ><span 
class="ptmri7t-">B.  Policy Iteration</span>
<a 
 id="Q1-1-21"></a>
<!--l. 66--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Error vs Iteration - Varying Gamma - Taxi-v3 - Policy Iteration.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-54r22"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;22.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 71--><p class="indent" >  </div><hr class="endfigure">
<!--l. 73--><p class="indent" >  Figure <a 
href="#x1-54r22">22<!--tex4ht:ref: cviusk --></a> shows an interesting interaction regarding the error found in the Policy Iteration algorithm with regard to the tuning of
gamma. As per Figure <a 
href="#x1-55r23">23<!--tex4ht:ref: iqcxde --></a>, the Policy Iteration algorithm found its greatest success with gamma being set high (a greater emphasis on
future rewards). However, the error as a function of iteration appeared to increase greatly per iteration. This is because as gamma
increases, the policy becomes more focused on maximizing long-term rewards. This can lead to more significant changes in the value
function between policy evaluation computations. These changes can typically cause the error to increase since the value
function is being updated using the Bellman optimality equation, which depends on the accuracy of all of the value
estimates.
<!--l. 79--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Reward vs Iteration - Varying Gamma - Taxi-v3 - Policy Iteration.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-55r23"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;23.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 84--><p class="indent" >  </div><hr class="endfigure">
<a 
 id="x1-56r3"></a>
<!--l. 86--><p class="noindent" ><span 
class="ptmri7t-">C.  Q Learning</span>
<a 
 id="Q1-1-23"></a>
<!--l. 88--><p class="indent" >  The graphs shown for the Q-Learning algorithm do not represent the best performances found with this algorithm on the Taxi
problem, but rather are here to depict interesting behaviours.
<!--l. 91--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Reward vs Iteration - Varying Gamma - Taxi-v3 - Q Learning - epsilon = 0.95.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-57r24"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;24.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 96--><p class="indent" >  </div><hr class="endfigure">
<!--l. 98--><p class="indent" >  The first graph to consider is Figure <a 
href="#x1-57r24">24<!--tex4ht:ref: ehfouy --></a> which demonstrates the same trend that was seen before; that when the gamma value is too
low, the value of future rewards is too heavily discounted, meaning that the agent focuses too much on near-term rewards resulting in
settling on suboptimal policies.
<!--l. 103--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Reward vs Iteration - Varying Epsilon - Taxi-v3 - Q Learning - gamma = 0.05.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-58r25"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;25.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 108--><p class="indent" >  </div><hr class="endfigure">
<!--l. 110--><p class="indent" >  The epsilon value is tweaked in Figure <a 
href="#x1-58r25">25<!--tex4ht:ref: obbavz --></a>, further analyzing the exploration-exploitation trade-off of the Q-Learning algorithm.
Interestingly, in this case, a low epsilon values allowed the algorithm to converge upon a better solution than did high epsilon values;
although convergence did occur in the cases of a very low gamma. It&#8217;s important to note that since gamma was so low in this case, this
means that the discount factor of future rewards is very punishing; this could indicate that future rewards could never be properly
found; or an understanding of the overall goal of the problem was never detected. Therefore, in this case, since the
end-goal was not findable (too much focus on short-term rewards), suboptimal policies were all that could be found; and
of those suboptimal policies, the best ones that were converged upon were those where the exploration rate stayed
low.
<!--l. 118--><p class="indent" >  <hr class="figure"><div class="figure" 
>
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  
<div  
class="centerline">                                                <img 
src="./images/Error vs Iteration - Varying Gamma - Taxi-v3 - Q Learning - epsilon = 0.95.png" alt="PIC"  
width="464" height="464" >                                                </div>
<a 
 id="x1-59r26"></a>
                                              <span 
class="ptmr7t-x-x-80">Fig.</span><span 
class="ptmr7t-x-x-80">&#x00A0;26.</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span>
                                                                                                  
                                                                                                  
<!--l. 123--><p class="indent" >  </div><hr class="endfigure">
<!--l. 128--><p class="indent" >  Two more interesting graphs were explored. Figure <a 
href="#x1-59r26">26<!--tex4ht:ref: kfhqig --></a> depicts how error changed with varying degrees of gamma and epsilon,
respectively. (Note that the epsilon graph was omitted for brevity, but it looks very similar.) As has been discussed before, the algorithm
appears to have greater changes and degrees of error when exploration rate is high. This is interestingly similarly high when gamma is
high, and intuitively makes sense because higher gamma means that there is a greater emphasis on considering long-term goals (less
discount of past rewards; more long-term thinking).
<a 
 id="x1-60r7"></a>
<!--l. 61--><p class="noindent" ><span 
class="ptmrc7t-">VII.  O<span 
class="small-caps">v</span><span 
class="small-caps">e</span><span 
class="small-caps">r</span><span 
class="small-caps">a</span><span 
class="small-caps">l</span><span 
class="small-caps">l</span> C<span 
class="small-caps">o</span><span 
class="small-caps">m</span><span 
class="small-caps">p</span><span 
class="small-caps">a</span><span 
class="small-caps">r</span><span 
class="small-caps">i</span><span 
class="small-caps">s</span><span 
class="small-caps">o</span><span 
class="small-caps">n</span></span>
<a 
 id="Q1-1-26"></a>
<!--l. 1--><p class="indent" >  In this report, reinforcement learning was studied experientially through a process of providing two well-known
Markov-Decision Process problems, and attempting to train agents to iteratively succeed in solving those problems.
The algorithms were compared to one another in terms of time, complexity, rewards versus iteration, and many other
metrics.
<!--l. 5--><p class="indent" >  Many interesting findings were unconvered, which helped elicit a deeper understanding of the pros and cons of each algorithm.
The Value Iteration and Policy Iteration tended to succeed in these toy examples, however considerable discussion
regarding why they succeeded and what their limitations might be were discussed at length. Several hypotheses were
made, and discussed. Of these, the results of experimentation allowed us to elicit interesting discussions to help address
them.
<!--l. 10--><p class="indent" >
     <ol  class="enumerate1" >
<li 
  class="enumerate" id="x1-62x1">
     <!--l. 10--><p class="noindent" >Value Iteration did tend to converge more quickly (in wall clock time) than did Policy Iteration and Q-Learning, since the
     value function in each iteration gets updated, and it uses a greedy policy which should be suitable for such a grid-world
     problem.
     </li>
<li 
  class="enumerate" id="x1-64x2">
     <!--l. 11--><p class="noindent" >Policy iteration did require fewer iterations than either Value Iteration or Q-Learning, although required more time per
     iteration than the others, particularly when the size of the model increased
     </li>
<li 
  class="enumerate" id="x1-66x3">
     <!--l. 12--><p class="noindent" >Unlike the prediction made, Q-Learning happened to not be as robust at solving the stochastic nature (slippery) of the
     Frozen  World  problem,  but  this  likely  can  be  attributed  to  hyperparameters  that  needed  to  be  tuned  better  to  increase
     exploration for larger state spaces. In general, considerable discussion was made regarding the value of Q-Learning of
     terms of being a model-free algorithm, and how this lack of model helps the algorithm succeed.
     </li>
<li 
  class="enumerate" id="x1-68x4">
     <!--l. 13--><p class="noindent" >All three algorithms performed well on the Taxi problem, although the Q-Learning algorithm required far more iterations
     generally.  Discussion  was  made  that  the  Value  Iteration  and  Policy  Iteration  algorithms  would  likely  suffer  should  the
     problem increase in state size or action size.
     </li>
<li 
  class="enumerate" id="x1-70x5">
     <!--l. 14--><p class="noindent" >The Q-Learning algorithm was indeed sensitive to the exploration / exploitation hyperparameters, and tuning them helped
     the problems become more robust against falling into suboptimal policies
     </li>
<li 
  class="enumerate" id="x1-72x6">
     <!--l. 15--><p class="noindent" >Both Policy Iteration and Value Iteration performed well on problems where the model was easy to predict, the transition
     matrix  (stochasticity)  was  known,  and  the  size  of  the  problem  was  relatively  small.  Increasing  the  size  of  the  problem
     drastically increased convergence time and space complexity for both.</li></ol>
<!--l. 1--><p class="indent" >
                                                                                                  
                                                                                                  
<!--l. 1--><p class="noindent" ><span 
class="ptmrc7t-">R<span 
class="small-caps">e</span><span 
class="small-caps">f</span><span 
class="small-caps">e</span><span 
class="small-caps">r</span><span 
class="small-caps">e</span><span 
class="small-caps">n</span><span 
class="small-caps">c</span><span 
class="small-caps">e</span><span 
class="small-caps">s</span></span>
<a 
 id="Q1-1-26"></a>
<!--l. 1--><p class="indent" >
   <div class="thebibliography">
   <p class="bibitem" ><span class="biblabel">
<span 
class="ptmr7t-x-x-80">[1]</span> <span class="bibsp"><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span></span></span><a 
 id="Xbellman1957markovian"></a><span 
class="ptmr7t-x-x-80">Richard Bellman.  A markovian decision process.  </span><span 
class="ptmri7t-x-x-80">Journal of Mathematics and Mechanics</span><span 
class="ptmr7t-x-x-80">, 6(5):679&#8211;684, 1957.</span>
   </p>
   <p class="bibitem" ><span class="biblabel">
<span 
class="ptmr7t-x-x-80">[2]</span> <span class="bibsp"><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span></span></span><a 
 id="XBertsekas:1996:NNL:560962"></a><span 
class="ptmr7t-x-x-80">Dimitri</span><span 
class="ptmr7t-x-x-80">&#x00A0;P. Bertsekas. Neuro-dynamic programming. In </span><span 
class="ptmri7t-x-x-80">Neuro-Dynamic Programming</span><span 
class="ptmr7t-x-x-80">, Optimization and Neural Computation Series. Athena Scientific,</span>
   <span 
class="ptmr7t-x-x-80">1996.</span>
   </p>
   <p class="bibitem" ><span class="biblabel">
<span 
class="ptmr7t-x-x-80">[3]</span> <span class="bibsp"><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span></span></span><a 
 id="X1606.01540"></a><span 
class="ptmr7t-x-x-80">Greg Brockman, Vicki Cheung, Ludwig Pettersson, Jonas Schneider, John Schulman, Jie Tang, and Wojciech Zaremba.  Openai gym, 2016.</span>
   </p>
   <p class="bibitem" ><span class="biblabel">
<span 
class="ptmr7t-x-x-80">[4]</span> <span class="bibsp"><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span></span></span><a 
 id="Xhart1968formal"></a><span 
class="ptmr7t-x-x-80">Peter</span><span 
class="ptmr7t-x-x-80">&#x00A0;E  Hart,  Nils</span><span 
class="ptmr7t-x-x-80">&#x00A0;J  Nilsson,  and  Bertram  Raphael.  A  formal  basis  for  the  heuristic  determination  of  minimum  cost  paths.  </span><span 
class="ptmri7t-x-x-80">IEEE  transactions  on</span>
   <span 
class="ptmri7t-x-x-80">Systems Science and Cybernetics</span><span 
class="ptmr7t-x-x-80">, 4(2):100&#8211;107, 1968.</span>
   </p>
   <p class="bibitem" ><span class="biblabel">
<span 
class="ptmr7t-x-x-80">[5]</span> <span class="bibsp"><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span></span></span><a 
 id="Xsutton2018reinforcement"></a><span 
class="ptmr7t-x-x-80">Richard</span><span 
class="ptmr7t-x-x-80">&#x00A0;S Sutton and Andrew</span><span 
class="ptmr7t-x-x-80">&#x00A0;G Barto.  </span><span 
class="ptmri7t-x-x-80">Reinforcement learning: An introduction</span><span 
class="ptmr7t-x-x-80">.  MIT press, 2nd edition, 2018.</span>
   </p>
   <p class="bibitem" ><span class="biblabel">
<span 
class="ptmr7t-x-x-80">[6]</span> <span class="bibsp"><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span><span 
class="ptmr7t-x-x-80">&#x00A0;</span></span></span><a 
 id="XWatkins1992"></a><span 
class="ptmr7t-x-x-80">C.</span><span 
class="ptmr7t-x-x-80">&#x00A0;J. C.</span><span 
class="ptmr7t-x-x-80">&#x00A0;H. Watkins.  Q-learning.  </span><span 
class="ptmri7t-x-x-80">Machine Learning</span><span 
class="ptmr7t-x-x-80">, 8(3-4):279&#8211;292, 1992.</span>
</p>
   </div>
   
</body></html> 

                                                                                                  



{% endraw %}


