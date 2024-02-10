# Start your research project

## Dataset

I had the option of using one of the five public datasets provided in the course (or my own). After careful consideration, I opted for the Mars craters dataset. This particular Mars Crater dataset [1] refers to a 2011 study of craters on Mars authored by Stuart James Robbins of the University of Colorado, Boulder [2].



## Research question

Although the data on morphology categories (MORPHOLOGY_EJECTA_1 through 3) are interesting, it's not accessible for the majority of the craters listed in the dataset. 
Therefore I have decided to analyze the geographic distribution of craters in terms of crater density and crater size (diameter). 

#### Question 1:
Is there a correlation between the location (longitude and latitude) and the amount of craters? In other words, is there a quadrant in which significantly more craters can be found?
For the analysis the surface of Mars will be divided into 4 quadrants: 
* Q1_NE: North-East
* Q2_SE: South-East
* Q3_SW: South-West
* Q4_NW: North-West   

<a href="https://ibb.co/bH0PRGt"><img src="https://i.ibb.co/YDC3TVg/Mars7.png" alt="Mars7" border="0" width="800"></a>

#### Question 2:
In regard to the first question: Is there a correlation between the most dense crater area (quadrant) and the biggest craters (diameter)?

## Code Book

Based on the original Mars Crater codebook [x] I wrote the following codebook:
# 
1. CRATER_ID: Crater ID for internal use, based upon the region of the planet (1/16ths), the “pass” under which the crater was identified, and the order in which it was identified.
2. LATITUDE_CIRCLE_IMAGE: Latitude from the derived center of a non-linear least-squares circle fit to the vertices selected to manually identify the crater rim (units are decimal degrees North).
3. LONGITUDE_CIRCLE_IMAGE: Longitude from the derived center of a non-linear least-squares circle fit to the vertices selected to manually identify the crater rim (units are decimal degrees East).
4. DIAM_CIRCLE_IMAGE: Diameter from a non-linear least-squares circle fit to the vertices selected to manually identify the crater rim (units are km).
5. Q1_NE: Quadrant 1 is North-East: Value of LONGITUDE_CIRCLE_IMAGE > 0 and value of LATITUDE_CIRCLE_IMAGE > 0
6. Q2_SE: Quadrant 2 is South-East: Value of LONGITUDE_CIRCLE_IMAGE > 0 and value of LATITUDE_CIRCLE_IMAGE < 0
7. Q3_SW: Quadrant 3 is South-West: Value of LONGITUDE_CIRCLE_IMAGE < 0 and value of LATITUDE_CIRCLE_IMAGE < 0
8. Q4_NW: Quadrant 4 is North-West: Value of LONGITUDE_CIRCLE_IMAGE < 0 and value of LATITUDE_CIRCLE_IMAGE > 0
# 

## References

[1] <a href="https://d3c33hcgiwev3.cloudfront.net/_b190b54e08fd8a7020b9f120015c2dab_marscrater_pds.csv?Expires=1707696000&Signature=RbFH9gp2GOZG1CUTMAnjX8mUf6agfE1gFF42EA2eE8qcKwb~lnbUZ6HaXJhG1tgTBbiGVkF6h-~Y148MgIkEetZnZR3Ir8lHfg~NGKxnCRJjxAOf-ZUBYIFS-ZTwNHK-ZUdPaYX0C2vX6jn4BmwYPm~6DfFhAqbti7WYy6NZReA_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A">Mars_Crater_Dataset</a>

[2] <a href="https://about.sjrdesign.net/files/thesis/RobbinsThesis_LargeMB.pdf">Robbins, S. J. (2011), Planetary Surface Properties, Cratering Physics, and the Volcanic History of Mars from a New Global Martian Crater Database., Site: Stuart Robbins, Astro/Geophysicist on the Web, 1–239</a>

[3] <a href="https://d396qusza40orc.cloudfront.net/phoenixassets/data-management-visualization/Mars%20Crater%20Codebook.pdf">CRATER_ID Codebook</a>

[4] <a href="https://onlinelibrary.wiley.com/share/TYIG4WKQTSHHQ22EZRHP?target=10.1111/maps.12895">Determination of Mars crater geometric data: Insights from high-resolution digital elevation models Peter J. Mouginis-Mark, Joseph Boyce, Virgil L. Sharpton, Harold Garbeil</a>

[5] <a href="https://agupubs.onlinelibrary.wiley.com/share/MCHMUXR6RTENP8AI7CUJ?target=10.1029/2011JE003967">A new global database of Mars impact craters ≥1 km: 2. Global crater properties and regional variations of the simple-to-complex transition diameter, Stuart J. Robbins, Brian M. Hynek</a>

[6] <a href="https://watermark.silverchair.com/spe550-29.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAxUwggMRBgkqhkiG9w0BBwagggMCMIIC_gIBADCCAvcGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM6EndwfiLBoyGU7bbAgEQgIICyKko3kL59exV54cgzGuJr9kS5dEQlxiFSukSiuVkghkpLXXf24FPufyTZw0PK7hY_cLKgrX-Z2LyvftDWL9purciovP9tfmCwgCc9VoCvKocmeL5dz6ykk-ElO1Vv0E66KhXjmMEKvgncg3t-j9V0wtjaMNQL-07EGSuwrSN5gWIRLS0ng26dzu6NV5-DulTQ7qbkAmWHxjft5F9qv8N-gyhUCu8vmIHcj767BjfGSaSWfr05_HoHxLEVvYJGY0nsm7CNu-CjxAi_ywTQ_SXjYXE0yyXaeIi5MauPge9A4lxW2PyMr9B97Yihta4lWOtY090PAXuSKPWmXBu__OafjL2B2ZsLgA2Mn0G6bgm2x0xuov2bQimrsKiRIP-rCpt9ItodLMfx39-oqD4MVd47UL_ngbUHwlWY528XlSny49Q_3JhId6QmV5mGffsQ1PoP7lptoa0bsHys3rePxcUQmi-1ust7w3xID6e2uOx_hiGNr2GVqBCZTRBMpBHztaaDTMYSEuHkwoDfXtWWeyTMPEvxUbzvVUkJ52_oOpiUDX_VsiyVB-a-dmBy12oOCEMvIkiR0-f3bpjjeXAB_Xl8KeA8UG6AEdIZ_HjVlWNbFqFt7zbNgEhGKSmLnd_cQaDpC_2GHC9ub16QvRii5vv4wqq48Ga6a0CN8xBIGiJVoNQi6Q-Kbm6B-dMg4Qvi1ueAFH-ICDpWb_BH7rzuxL5FoGNr6wH2cdTDy-08gluhcrhcpzyThKH24wVquVKnOFFhR8CxSx7_C59kKm9fEDAl_HdPY5YsyYHzBNpIoeyizaANh8cGUIwNhb07-BNukRtVHfq79_fSIFXW1NYCnzj6RO3el3XaJ-pMJHmcBywnt_k4TD-1VY4I1PFUQ-brqOdnNnwRJgOHH5x12jSjfDW0-n0Vh-kptcDfnuf3JX5NpCTxqOY8WgTnv8"> Mars Crater Database: A participative project for the classification of the morphological characteristics of large Martian craters</a>

