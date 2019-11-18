def percentage(score, total):
    assert total > 0, 'total doit être strictement positif'
    assert 0 <= score, 'score doit être positif'
    assert score <= total, 'score doit être inférieur à total'
    return score / total * 100

print(percentage(15, 20), '%')
print(percentage(22, 20), '%')