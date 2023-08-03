import numpy as np
from torchmetrics.text import BLEUScore
from rouge import Rouge
def Evaluate_text(pred,target_ref):
    bleu = BLEUScore()
    rouge = Rouge()
    str_pred = ' '.join(map(str, pred))
    str_target = ' '.join(map(str, target_ref))
    rouge_score = rouge.get_scores(str_pred, str_target)
    bleu_score=bleu(pred, target_ref)
    print("Bleu score : ",bleu_score)
    print("Rouge score : ")
    print(rouge_score)
    return bleu_score,rouge_score
preds = ['the cat is on the mat']
target = [['there is a cat on the mat', 'a cat is on the mat']]
Evaluate_text(preds,target)