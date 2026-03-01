from engine import EITScoringEngine

def run_demo():
    engine = EITScoringEngine()
    ref = "El niño está jugando en el jardín"
    stu = "El niño está jugado en el jardín"
    score = engine.score(stu, ref)
    print(f"Test Successful! Standardized EIT Score: {score}/3")

if __name__ == "__main__":
    run_demo()