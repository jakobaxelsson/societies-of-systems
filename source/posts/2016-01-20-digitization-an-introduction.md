---
layout: post
title: "Digitization: An introduction"
date: 2016-01-20
categories:
---

_One of the most important trends in society today is the digitization of almost everything. It is also the trend that makes systems-of-systems an urgent topic. But what is digitization all about? Here, I will give an overview of what I perceive as some of the most important trends that make digitization happen today, as well as some of the challenges._

On Nov. 24, 2015, I had the honor of addressing a group of some 200 key decision makers in the automotive industry at the annual conference of the [Swedish vehicle research and innovation program (FFI)](https://www.vinnova.se/m/fordonsstrategisk-forskning-och-innovation/). The topic I was asked to talk about was _digitization_, to give the audience an understanding of what it is and why it is happening right now. The talk was in Swedish, and can be seen [online](https://www.youtube.com/watch?v=3uzEVDFmOYQ&index=4&list=PLI7DD2rwMEJ6dMZcwoIRM429p0sGO1VOt). In this post, I will summarize some of the topics I brought up in the talk, as a background on digitization that is important to understand the challenges related to systems-of-systems.

Digitization is a trend that is affecting everybody and every part of society, and due to the many uncertainties connected to it, a lot of people are experiencing what one might call a _“digital anxiety”_. The effects will be large, some thinkers are suggesting that we will all be out of jobs, and that the gaps between rich and poor will increase. Others, on the contrary, argue that this could be the beginning of a new golden age, where new and better jobs will replace the old ones. Politicians are talking about a new industrialization where the digital technology is breathing new life into manufacturing.

In my work as a researcher, I often meet professionals who describe a similar digital anxiety, but from the perspective of their company. They ask questions such as: How should we relate to the new technology? How will the market and business models change? Will Google or some other actor steal our customers? Of course, nobody knows the answers to these questions, but the best one can do is to increase one’s knowledge of the underlying forces. My target with this post is to briefly summarize the technical trends that are behind industrialization, and point at some challenges for industry, in particular manufacturing companies as exemplified by the automotive business.

Technical trends
----------------

So what is behind digitization? Well, in essence, it is a technology development that has been going on at an even pace for a long time, and which is often referred to as _Moore’s law_. This well known trend is 50 years old, and says, a bit simplified, that the performance of electronics doubles every second year without increasing the cost. The below graph shows this development from 1970 to today. Note that the y axis is logarithmic, so that today’s electronics has _10 million times_ the performance of the technology 50 years back. This means that it is all the time becoming possible to perform faster calculations, store and send more data, and provide more sensors at the same cost.

![Moores law](/assets/moores-law.png)

A similar development can be seen for _Internet bandwidth_, as shown in the next graph. Communication is now so fast that it pays off to build very distributed systems. Data can be gathered in one place, and processed or stored in another, while being presented in a third.

![Internet connectivity](/assets/internet-connectivity.png)

It has also become cheap to put powerful _sensors_ on physical things. The next graph shows how the sensor industry predicts that the number of sensors will grow over the next ten years, from ten billion today to ten trillion. With improved communication, it becomes possible to access the data from a distance, which increases the value of the sensors.

![Sensor trend](/assets/sensor-trend.jpg)

Lots of sensors produce lots of data that can now be gathered in the same place. Big data is a popular term for this, which also relates to the influential power provided by having access to data. Note in the next graph that the y-axis is linear, so this is what an exponential growth really looks like.

![Global data](/assets/global-data.jpg)

System trends
-------------

So what are the consequences of these technology trends on how systems are built? One consequence is that it becomes interesting to put plenty of sensors on physical items, and connect them to the Internet, which is often referred to as the _Internet of Things._ Examples of this can be found in building automation, so called smart homes, but similar solutions are discussed in many industries.

Access to computational resources has also become very flexible through _cloud computing_. In essence, this is just large server halls where users can buy capacity instead of buying their own computers. But this leads to extremely low entrance thresholds for new IT companies, since almost no capital investments are required. Instead, more computational power is rented as demand is increasing.

To have any use for all the data that these systems generate, it must be processed, but this is challenged by the limitations of our ability to develop _algorithms_ that can solve complex problems. Instead of hand crafting algorithms, advanced techniques from _artificial intelligence_ such as machine learning are needed, to automatically find interesting information in all the data. Simply speaking, this means that the computer is not told how to solve the task, but instead it is trained on a number of examples to find patterns. Like many of the issues already described above, these are old techniques, but it is only now that there are sufficient computational resources available to solve interesting, real-life problems. It is also only now that there is sufficient amount of data to train the algorithms.

One important factor why digitization is happening now, and not before, is also that cheap, powerful, and always connected terminals have become available for most people through _smart phones_. This increases the potential clientele for digital services, and increases the time and place where those services are available, since they no more require that we are using them in front of our computers.

Last but not least has the standards for software matured, and in particular the standards used on the web. This makes it very easy to give a system a _data interface_ towards other systems. One very important development in this is that it now becomes possible to view a system as a component in a larger _system-of-systems_.

Benefits
--------

So what _benefits_ is it that people try to achieve through digitization? Well, if you scratch the surface and try to find common factors, the services are often about _automation of workflows_. It is about connecting different systems to a system-of-system, where data is transmitted automatically between the parts, whereas before a person had to move the data manually. Along the way, automatic data processing is also introduced, that can make better decisions than humans due to a more detailed world view. It further becomes faster, more predictable, and eliminates the risk for human mistakes. One example of companies utilizing this is [Klarna](http://www.klarna.se/) to make extremely fast and accurate credit assessments.

Another type of efficiency improvement is to _better match supply and demand_. Companies like [Uber](http://www.uber.com/) and [AirBnB](http://www.airbnb.com/) make unused resources in the form of cars and beds available for customers who could perhaps not afford a traditional taxi or hotel.

A third effect is the possibility to open up the systems for external extensions, which is sometimes referred to as _open innovation_. A good example of this is the possibility to download apps from third party developers in a smart phone, but similar possibilities exist also in other types of systems. The base system developer gets a more attractive product that can be customized for many uses. The app developer gets a market for their ideas. The customer gets a broader range of products to choose from. One can reason in similar ways regarding sharing of data and the creation of open service interfaces.

Consequences for industry
-------------------------

So what are the consequences for the manufacturing industries like the automotive business? One major concern is to what extent companies want to, and dare to, _open up_ their products. This question is partly technical, focusing on what the system architecture should look like to be able to handle openness. But it also contains business concerns. Do you _want_ to continue to “own” the customer, i.e. put your company in the center of the picture? _Can_ you even own the customer? I do not believe that this will work in the future. Instead, I believe that we will increasingly view products such as cars as components in systems-of-systems, where they interact with other similar products (other cars); with the OEM’s cloud services; with public services; and with services from third parties. Focus will be moved from the individual products, to the larger context where the product is residing.

Connected to this is also the OEM’s _strategy for handling partners_. Who do you want to work with in order to offer attractive services? How will you handle an increasingly fragmented landscape, where new actors rapidly appear, and then maybe disappear again? Where the software lifecycle is completely different from that of the physical product. _Speed and flexibility_ will become keywords.

A third aspect that I would like to emphasize is how to make the systems _trustworthy_. In the future, many products will become _reliant on other actors’_ data, software and services. These will change at an increasingly higher pace, and the OEM will not be able to apply quality assurance in the same way as they do to physical components from suppliers today. So how can you ascertain that it is safe to use a product such as a vehicle as a component in a system-of-systems? Who is responsible for quality? How do you test it? My research indicates that there is a need to work with more dynamic solutions, where data is continuously brought back from operations, where incidents are evaluated before they become accidents, and where improved software is rapidly deployed to products in the field.

So to conclude, it is apparent that digitization is a development that results from improved technology, and fundamentally by Moore’s law. However, the challenges for industry concern to a large extent how the technology can best be applied to the business, and how to do systems engineering under these new circumstances.