# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

def solution(price, money, count):
    tot = (price + count*price)*count/2
    answer = (tot-money)
    return(0) if answer <= 0 else int(answer)


solution(3,20,4) 
