from math import sqrt
#from handcalcs import handcalc
import streamlit as st

#@handcalc
def quadratic(a,b,c):
    x_1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x_2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    racines = (x_1 , x_2)
    return racines

a = st.slider("Value for a:", 1,5, 2)
b = st.slider("Value for b:", -10, 10, -5)
c = st.slider("Value for c:", -10,10, -5)

st.title("Equation du second degré")
if b>0 and c>0 :
    st.latex(f"{a}x^2 + {b}x + {c} = 0")

if b<0 and c<0 :
    st.latex(f"{a}x^2 {b}x {c} = 0")

if b<0 and c>0 :
    st.latex(f"{a}x^2 {b}x + {c} = 0")

if b>0 and c<0 :
    st.latex(f"{a}x^2 + {b}x {c} = 0")

#st.latex(f"{a}x^2 + {b}x + {c} = 0")

vals = quadratic(int(a),int(b),int(c))
#st.latex(latex_code)
st.write("Vals from returned dict:")
st.write("x_1:", vals[0], "x_2:", vals[1])
