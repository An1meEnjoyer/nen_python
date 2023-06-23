# Python nen
Simple code realisation of nen from hunter x hunter

## Intro
hunter x hunter is my favorite anime. So I code the technique of nen in python
## Logic
**Object, Aura**:
Classes that describe objects "outside" your body. Like chains or fireball.

**Nen, Ten, Zetsu, Ren, Hatsu**: Classes that describe things "inside" your body. Like how many aura you have and what you wanna do with it. 

**Nen** - base class, creates aura even for "non-users". But for them aura flows outside their bodys.

**Zetsu** - child class of Nen. Allows you to hide your aura.

**Ten** - child class of Nen. Allows you to control aura and slow down passive outflow.

**Ren** - child class of Ten. Allows you to more accurate control your aura. Now you can focus the aura in each part of the body separately.

**Hatsu** - child class of Ren. Now you finally can cast unique abilities. 
## Usage/Examples
First we need to "learn" Hatsu:
```
hatsu = Hatsu()
```

Now let's cast Kurapika's chains.

Make a chain and enhant it by 10 abstract points:
```
chain = hatsu.create(Object())
chain = hatsu.enhant(chain, 10)
```
Now we can throw it for example by 4 meters:
```
chain = hatsu.manipulate(chain, 0, 4)
```
*Congratulations!* We make Kurapika's chains and threw them :)

To make Killua's electricity we can do:
```   
aura = hatsu.emit(Aura())
aura = hatsu.transmute(aura, 'electricity')
```
Now we have electricity aura!

By doing all this, our aura score is reduced, but it can be restored.
