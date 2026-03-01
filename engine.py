from sentence_transformers import SentenceTransformer
import language_tool_python
from sklearn.metrics.pairwise import cosine_similarity

class EITScoringEngine:
    def __init__(self, weights={'content': 0.7, 'mechanics': 0.3}):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.tool = language_tool_python.LanguageTool('es')
        self.weights = weights

    def evaluate_content(self, student, ref):
        stu_emb = self.model.encode([student])
        ref_emb = self.model.encode([ref])
        return cosine_similarity(stu_emb, ref_emb)[0][0]

    def evaluate_mechanics(self, text):
        matches = self.tool.check(text)
        word_count = max(1, len(text.split()))
        return max(0, 1 - (len(matches) / word_count))

    def score(self, student_text, ref_text):
        content = self.evaluate_content(student_text, ref_text)
        mechanics = self.evaluate_mechanics(student_text)
        raw = (content * self.weights['content']) + (mechanics * self.weights['mechanics'])
        return round(raw * 3)