#ESM Translator

##Cos'è

ESM translator è un programma per uso privato. Le funzionalità che offre sono quelle, dato in input un file esm di:

- processarne il testo tramite la libreria python `bethesda-struct`

- inviare le stringhe ad un traduttore basato su intelligenza artificiale e tradurre

##Come funziona

Il programma riceve in input il path del file esm e restituisce in output un file traduzioni

##Limitazioni

AI translator permette la traduzione gratuita fino a 500.000 caratteri al mese. Al fine di rendere l'utilizzo del traduttore gratuito ESM translator misura il numero di caratteri tradotti ogni mese e una volta raggiunto il limite blocca le funzionalità fino al mese successivo

####Bethesda-struct

Documentazione al [link](https://pypi.org/project/bethesda-structs/)

####Dettagli Google Cloud Translation

Per maggiori informazioni riguarda la documentazione al [link](https://cloud.google.com/translate/?hl=it&utm_source=google&utm_medium=cpc&utm_campaign=emea-it-all-it-dr-bkws-all-all-trial-e-gcp-1011340&utm_content=text-ad-none-any-DEV_c-CRE_170511603325-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20AI%20%26%20ML%20~%20Cloud%20Translation%23v2-KWID_43700053287028084-aud-606988877734%3Akwd-14329410560-userloc_20590&utm_term=KW_google%20translate%20api-NET_g-PLAC_&gclid=CjwKCAjwkYGVBhArEiwA4sZLuAWJV6a1Q7KO_XcXVVXfW2T-bvuwSuDeezf8MCxOzNaXGezWzZGi8hoCnFAQAvD_BwE&gclsrc=aw.ds#section-6): 

![Opzioni di traduzione](\img\costi_translation_ai.png)

![Costi di traduzione per l'opzione basic](\img\costi_translation_basic.png)