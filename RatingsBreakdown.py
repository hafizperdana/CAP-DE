from mrjob.job import MRJob
from mrjob.step import MRStep

class RatingsBreakdown(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings),
            MRStep(reducer=self.output)
        ]

    def mapper_get_ratings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield rating, 1

    def reducer_count_ratings(self, key, values):
        yield None, (sum(values), key)

    def output(self, _, rating_counter):
        for count, rating in sorted(rating_counter, reverse=True):
            yield rating, count

if __name__ == '__main__':
    RatingsBreakdown.run()