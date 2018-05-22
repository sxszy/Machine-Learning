"""
Auther: szy
Date: 2018/4.23
"""

#import
import Orange

## Read the file
data = Orange.data.Table("mammographic_masses.csv")
rules = Orange.associate.AssociationRulesSparseInducer(data, support=0.01, confidence=0.01)
print ("%4s %4s  %s" , "Supp", "Conf", "Rule")
for r in rules:
    print ("%.2f %.2f  %s", r.support, r.confidence, r)
    
