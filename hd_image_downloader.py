#download first 30 photos from Pexel with the given search term

import requests, os, bs4

def hd_imageDownloader(word, folder):

	url = 'https://www.pexels.com/search/' + word + '/'
	os.makedirs(folder, exist_ok=True)
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	#all_images = soup.select('.js-photo-link > .photo-item__img')
	all_href = soup.select('.js-photo-link')
	if all_href == 0:
		print('No photos were found')
	else:
		try:
			for i in range(len(all_href)):
				picHref = all_href[i].get('href')
				picUrl = 'https://www.pexels.com' + picHref
				res = requests.get(picUrl)
				res.raise_for_status()
				soup = bs4.BeautifulSoup(res.text, 'html.parser')
				bigImage = soup.select('.js-photo-page-image-img')
				bigPicSrc = bigImage[0].get('src')
				imageName = word + str(i) + '.jpeg'
				print('\nDownloading image %s...' % (imageName) + '\n')
				res = requests.get(bigPicSrc)
				res.raise_for_status()
				folderWithImages = open(os.path.join(folder, imageName), 'wb')
				for chunk in res.iter_content(1000000):
					folderWithImages.write(chunk)
				folderWithImages.close()
		except requests.exceptions.MissingSchema:
			print('Error occured')

searchWord = input('What would you like to search? ')
folderName = input('How would you like to name the folder? ')

hd_imageDownloader(searchWord, folderName)	
