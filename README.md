# Notes

Excluded (don't have "sent_items" folder):
    ./maildir\dickson-s
    ./maildir\fossum-d
    ./maildir\guzman-m
    ./maildir\hain-m  
    ./maildir\harris-s
    ./maildir\hyvl-d
    ./maildir\linder-e
    ./maildir\merriss-s
    ./maildir\rodrique-r
    ./maildir\south-s
    ./maildir\stclair-c
    ./maildir\stokley-c
    ./maildir\symes-k
    ./maildir\whalley-l

Assume that items in the sent folder are sent from the owner (name) of the parent folder 
    i.e. all emails in ./maildir/tholt-j/sent_items were sent from tholt-j

Removed maildir\\pereira-s\\sent_items\\clickathome

Output from SNA.py:
    Nodes:  5472
    Edges:  13036
    Avg Clustering:         0.2449055986962845
    Connected Components:   1
    Diameter:       6
    Radius:         3
    Avg Shortest Path Length:       3.4418203611600133
    Density:        0.0008708864710365446
                        Address    Degree  Eigenvector  Betweenness  Closeness
    0         k..allen@enron.com  0.018644     0.095670     0.013789   0.405439
    1    karen.buckley@enron.com  0.005118     0.044036     0.001852   0.356046
    2     jeanie.slone@enron.com  0.004021     0.048959     0.001320   0.371142
    3     faith.killen@enron.com  0.001097     0.022763     0.000018   0.341042
    4  jennifer.fraser@enron.com  0.001462     0.022690     0.000088   0.345828