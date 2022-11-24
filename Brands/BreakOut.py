import Functions
import pandas as pd


def get_detail(soup, pname):
    product_deatil = {pname: [], f'Price_{pname}': []}
    for i in soup:
        try:
            name = i.find('a').text
            try:
                price = i.find('span', attrs={'class': 'old-price'}).text
                if price == "":
                    raise Exception
            except:  # if "old-price hide" in i:

                price = i.find('div', attrs={'class': 'pt-price'}).text.split(' ')[-1]
            product_deatil[pname].append(name)
            product_deatil[f'Price_{pname}'].append(price)
        except:
            pass
    return pd.DataFrame(product_deatil)


Tees = "https://breakout.com.pk/collections/men-tees?view=all"
soup_tees = Functions.get_soup_from_selenium(Tees)
flex_tees = soup_tees.find_all('div', attrs={'class': 'pt-description'})[1:]
df_Tees = get_detail(flex_tees, "Tees")

Polo = "https://breakout.com.pk/collections/men-polos?view=all"
soup_polo = Functions.get_soup_from_selenium(Polo)
flex_polo = soup_polo.find_all('div', attrs={'class': 'pt-description'} )[1:]
df_Polo = get_detail(flex_polo, "Polo")

Jeans = "https://breakout.com.pk/collections/men-denim?view=all"
soup_Jeans = Functions.get_soup_from_selenium(Jeans)
flex_Jeans = soup_Jeans.find_all('div', attrs={'class': 'pt-description'})[1:]
df_Jeans = get_detail(flex_Jeans, "Jeans")

df = pd.concat([df_Tees, df_Jeans, df_Polo, ], axis=1)
print(df)
# df.to_excel("BreakOut.xlsx", index=False)
