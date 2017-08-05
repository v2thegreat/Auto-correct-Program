# Auto Correct

## What is it?

This is a python script that takes in a sentence, finds the incorrect words while compariring them to a list of words (presumibly from a file), uppercases them, and returns the possible correct suggestions

## Why?

An Auto Correct program is a commmonly used program in most mobile phones (you also have auto complete, but that one predicts, not corrects).

## How do I use it?

```
autocorrect('Hi. Ths is a sentence')

Hi. THIS is a sentence
['this']
>>>
```

## What if I want to expand the dictionary of usable words?

Change the first line:

```
Correct_Word_List=['hi','this','is','a','sentence']
```

to

```
Correct_Word_List=open('<File Name>.txt').readlines()
```

where the <File name>.txt is a file which has words to be corrected against

**Note:** However, ensure that most of the words are:

  * **In Lowercase:** This isn't very important, but you might have the issue where it isnt able to properly identify and compaire the words

  * **Seperated by a new line**: This is just to highlight a need for a proper seperator, where each word can be read. A user can simply rewrite:

	```
	Correct_Word_List=['hi','this','is','a','sentence']
	```

	or

	```
	Correct_Word_List=open('<File Name>.txt').readlines()
	```

	to

	```
	Correct_Word_List=open('<File Name>.txt').read().split('<Seperator>')
	```
