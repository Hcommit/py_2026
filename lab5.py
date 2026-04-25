"""
Amazon.com monitors their website response times during festival sales.
They collect response times (in milliseconds) for 10 random page loads during peak traffic hours.

Response Times (ms): [245, 312, 189, 276, 298, 234, 389, 267, 301, 223]

Compute the Average response time (Mean) and inconsistent performance (Standard Deviation).
"""

import math

# Response times in milliseconds
responseTimes = [245, 312, 189, 276, 298, 234, 389, 267, 301, 223]

# Calculate mean (average)
total = sum(responseTimes)
numResponses = len(responseTimes)
meanTime = total / numResponses

# Calculate standard deviation
sumSquaredDiff = 0
for time in responseTimes:
    sumSquaredDiff += (time - meanTime) ** 2

stdDeviation = math.sqrt(sumSquaredDiff / numResponses)

# Display results
print("Response Times (ms):", responseTimes)
print("Average Response Time (Mean):", round(meanTime, 2), "ms")
print("Inconsistent Performance (Standard Deviation):", round(stdDeviation, 2), "ms")