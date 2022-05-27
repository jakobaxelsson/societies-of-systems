---
layout: post
title: "Orchestration vs. choreography in systems-of-systems"
date: 2016-11-29 12:00:00 -0000
categories:
---

When creating an SoS, there is usually a certain functionality or capability which is sought. This functionality emerges as a consequence of the collaboration that the constituent systems engage in. The functionality does however not emerge out of the blue, but it has to be designed like any other engineered system. In some way, the constituents have to be told what they should do or how they should behave in order for the SoS to reach its objectives. How this information should be conveyed to the constituents is a fundamental design decision, which is sometimes also limited by the context of the SoS, including what authority the different stakeholders have in relation to each other.

There have been attempts to identify recurring patterns, or archetypes, that are common in SoS with respect to this coordination. The most influential set of archetypes was initially proposed by Maier ([1996](https://archive.is/Rcc6e), [1998](https://www.google.se/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjT7Z7pqc3QAhUGKMAKHYGHBUgQFggiMAA&url=https%3A%2F%2Fwww.researchgate.net%2Ffile.PostFileLoader.html%3Fid%3D54db580fd5a3f2265f8b4609%26assetKey%3DAS%253A273698123124736%25401442266126003&usg=AFQjCNHkvDHWf8OeNK163ABx11GRMpfNpw)), and then extended by [Dahmann and Baldwin (2008)](http://ieeexplore.ieee.org/document/4518994/). It is based on the authority and responsibility in managing the evolution of the SoS, and consists of the following archetypes, as interpreted by [Lane and Epstein (2013)](https://www.google.se/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwi1uLjYq83QAhWrIMAKHcxnChUQFggdMAA&url=http%3A%2F%2Fcsse.usc.edu%2FTECHRPTS%2F2013%2Freports%2Fusc-csse-2013-500.pdf&usg=AFQjCNHMx-yFJ1Kh0Xq_XiTnpmDCCc7QRg):

*   _Directed_: The SoS is built for a specific purpose, and has a dedicated central management. The constituent systems retain their individual capabilities but are normally subordinated to the SoS.

*   _Acknowledged_: The SoS is built for specific purpose (similar to directed), and has central management in the form of a dedicated organization. However, the constituent systems are not normally subordinated (similar to collaborative). Typically, it is a result of building an SoS out of a combination of existing and new systems. Evolution takes place through collaboration between the constituent systems’ owners.

*   _Collaborative_: The SoS has an agreed upon purpose, and central management, but with limited power. Typically, the central management is formed through a cooperation between the organizations behind the constituent systems, rather than being a dedicated organization for the SoS. The constituent systems collaborate voluntarily to fulfil the agreed upon purposes.

*   _Virtual_: There is no agreed upon SoS purpose and no central management. The SoS behavior is emergent, and not caused by explicit mechanisms. The formation is ad hoc and the constituent systems are not necessarily known.

The virtual archetype is somewhat questionable, since it can be discussed if an SoS without a purpose is even to be considered a system. The example of a virtual SoS proposed in the literature is the World Wide Web. On the other extreme, a very directed system would probably have constituents with very limited use outside the SoS context, and hence it is more of a system than an SoS.

In a directed SoS, the central management organizations typically define the design of the constituent systems, whereas in the acknowledged archetype, it reaches agreements with the organizations responsible for the constituent systems.

Although this set of archetypes gives interesting perspectives on the power distribution in an SoS, it does not provide details about how the information about desired behavior is conveyed to the constituents. However, in the domain of _service-oriented architecture_ (SOA), this has been discussed using the concepts of _orchestration_ and _choreography_. The differences between these two concepts are as follows (as explained [here](http://stackoverflow.com/questions/4127241/orchestration-vs-choreography)):

*   _Orchestration_: A single centralized component (called the orchestrator) coordinates the interactions between the other components. It is thus responsible for implementing the SoS services.

*   _Choreography_: A global description is created, which contains information about the participating components, the information exchanges between them, rules of interaction, and agreements between them. This description is used by all the participating components, and thus constitutes a decentralized approach. In practice it could be implemented in different ways, e.g. as a specification document, a software plug-in, or a data file read by a generic interpreter.

The parallel to the SoS archetypes is pretty obvious: a directed SoS is designed as an orchestration, whereas a virtual SoS is based on choreography. The other archetypes constitute a mix of the two.

Personally, I have always found the SoS archetypes difficult to apply in practice, possibly since most concrete SoS examples are in the mixed categories, and these are not very distinct. Possibly, a route forward is to instead refine the concepts of orchestration and choreography to concretize for a given case how collaboration actually is coordinated?