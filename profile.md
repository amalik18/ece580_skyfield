`cProfile` run for the `track_sat` command, with the Top 10 most called functions

```bash
         500487 function calls (486762 primitive calls) in 6.843 seconds

   Ordered by: call count

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    51005    0.007    0.000    0.007    0.000 einsumfunc.py:989(_einsum_dispatcher)
26095/24047    0.043    0.000    0.143    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
    17934    0.002    0.000    0.002    0.000 {built-in method builtins.isinstance}
16380/15776    0.002    0.000    0.002    0.000 {built-in method builtins.len}
    14473    0.004    0.000    0.004    0.000 {built-in method builtins.getattr}
    13944    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
12050/5050    0.009    0.000    0.433    0.000 descriptorlib.py:9(__get__)
    10001    0.004    0.000    0.058    0.000 einsumfunc.py:997(einsum)
    10001    0.005    0.000    0.084    0.000 <__array_function__ internals>:177(einsum)
    10001    0.054    0.000    0.054    0.000 {built-in method numpy.core._multiarray_umath.c_einsum}
 ```

---

`cProfile` run for the `track_planet` command, with the Top 10 most called functions

```bash
         551110 function calls (537214 primitive calls) in 4.073 seconds

   Ordered by: call count

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    49009    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
    36005    0.004    0.000    0.004    0.000 einsumfunc.py:989(_einsum_dispatcher)
    22268    0.005    0.000    0.006    0.000 {built-in method builtins.getattr}
20063/19035    0.032    0.000    0.083    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
    17503    0.002    0.000    0.002    0.000 {built-in method builtins.isinstance}
15857/15253    0.002    0.000    0.002    0.000 {built-in method builtins.len}
    14840    0.054    0.000    0.054    0.000 {built-in method builtins.divmod}
    12000    1.790    0.000    1.911    0.000 spk.py:201(generate)
10464/3464    0.009    0.000    0.352    0.000 descriptorlib.py:9(__get__)
    10000    0.001    0.000    0.001    0.000 multiarray.py:736(dot)
```

---

`cProfile` run for the `track_asteroid` command with the Top 10 most called functions

```bash
        518957 function calls (506244 primitive calls) in 2.389 seconds

   Ordered by: call count

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    37945    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
    36005    0.004    0.000    0.004    0.000 einsumfunc.py:989(_einsum_dispatcher)
21059/20031    0.033    0.000    0.088    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
    18487    0.002    0.000    0.002    0.000 {built-in method builtins.isinstance}
    17146    0.005    0.000    0.005    0.000 {built-in method builtins.getattr}
15850/15246    0.002    0.000    0.002    0.000 {built-in method builtins.len}
    13126    0.003    0.000    0.003    0.000 {built-in method builtins.hasattr}
10403/4403    0.009    0.000    0.358    0.000 descriptorlib.py:9(__get__)
    10000    0.001    0.000    0.001    0.000 multiarray.py:736(dot)
    10000    0.006    0.000    0.024    0.000 <__array_function__ internals>:177(dot)
```

---

`cProfile` run for the `track_voyager` command with the Top 10 most called function

```bash
         526292 function calls (513120 primitive calls) in 1.344 seconds

   Ordered by: call count

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    38101    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
    36005    0.004    0.000    0.004    0.000 einsumfunc.py:989(_einsum_dispatcher)
21059/20031    0.033    0.000    0.087    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
    18488    0.002    0.000    0.002    0.000 {built-in method builtins.isinstance}
    17452    0.005    0.000    0.005    0.000 {built-in method builtins.getattr}
15851/15247    0.002    0.000    0.002    0.000 {built-in method builtins.len}
    14126    0.003    0.000    0.003    0.000 {built-in method builtins.hasattr}
10556/4556    0.010    0.000    0.360    0.000 descriptorlib.py:9(__get__)
    10000    0.001    0.000    0.001    0.000 multiarray.py:736(dot)
    10000    0.006    0.000    0.025    0.000 <__array_function__ internals>:177(dot)
```