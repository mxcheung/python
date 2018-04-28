# Computes the histogram of a set of data
def histogram(data, num_bins):
 
    # Find what range the data spans, and use it to calculate the bin size.
    span = max(data) - min(data)
    bin_size = span / num_bins
 
    # Calculate the thresholds for each bin.
    thresholds = [0] * num_bins
    for i in range(num_bins):
        thresholds[i] += (bin_size * (i+1)) + min(data)
 
    # Compute the histogram
    counts = [0] * num_bins
   
    prevthreshold =  min(data);
    for datum in data:
        # Increment the count of the bin that the datum falls in
        for bin_index, threshold in enumerate(thresholds):
         
            if  (datum >= threshold - bin_size )   and (datum <= threshold) :
                counts[bin_index] += 1
                prevthreshold = threshold;
    return counts
 
# Some random data
data = [-3.2, 0, 1, 1.5, 1.6, 1.9, 5, 6, 9, 1, 4, 5, 8, 9, 5, 6.7, 9]
print("Correct result:\t" + str([1, 6, 4, 6]))
print("Your result:\t" + str(histogram(data, num_bins=