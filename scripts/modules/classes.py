class Element():
    def __init__(self, position, vector, pLDDT):
        self.position = position
        self.vector = vector
        self.pLDDT = pLDDT

    def get_position(self):
        return self.position

    def get_vector(self):
        return self.vector

    def get_pLDDT(self):
        return self.pLDDT

    def score_xavi(self, lenseq):
        position=self.get_position()
        max=lenseq-2
        if 2<position and position<max:
            mynums=self.get_vector()[position-3:position+2]
            score=sum(mynums)/len(mynums)
        else:
            score=2
        return score

    # def score_xavi2(self, max):
    #     # max=lenseq here so when call that function pass lenseq. ex: final_scores.append(element.score_xavi2(lenseq))
    #     position=self.get_position()
    #     if 0<position and position<max:
    #         score=self.get_vector()[position]-self.get_vector()[position-1]
    #     else:
    #         score=1
    #     return score
