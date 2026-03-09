# How to use the code
The following code is a CLI extension used to compute the amount of A and B components to make the expected weight of PDMS. 

The following will run the default which is 10 g of PDMS with a ratio 10:1 of A:B

```shell
pdms-ratio.exe 
```

If you want to specify the weight for a default ratio of 10:1 the following is an example for a 100 g PDMS weight

```shell
pdms-ratio.exe 100
```

And if you want to specify either A and/or B 

```shell
pdms-ratio.exe --a-ratio 14
```

```shell
pdms-ratio.exe --b-ratio 3
```

```shell
pdms-ratio.exe --a-ratio 14 --b-ratio 3
```

And if you want to combine all of them you do it as follows

```shell
pdms-ratio.exe 212.53 --a-ratio 14 --b-ratio 3
```

This will compute the amount for A and B to maintain a 14:3 ratio for a total PDMS weight of 212.53 g.