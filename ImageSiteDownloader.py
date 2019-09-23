#download first 30 photos from Pexel with the given search term

import requests, os, bs4

def imageDownloader(word, folder):
	url = 'https://www.pexels.com/search/' + word + '/'
	os.makedirs(folder, exist_ok=True)
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, 'html.parser')

	all_images = soup.select('.js-photo-link > .photo-item__img')

	for i in range(len(all_images)):
		picSrc = all_images[i].get('src')
		imageName = picSrc[33:36] + '.jpeg'
		print('\nDownloading image %s...' % (picSrc) + '\n')
		res = requests.get(picSrc)
		res.raise_for_status()	
		folderWithImages = open(os.path.join(folder, imageName), 'wb')
		for chunk in res.iter_content(1000000):
			folderWithImages.write(chunk)
		folderWithImages.close()
	return len(all_images)
	
searchWord = input('What would you like to search? ')
folderName = input('How would you like to name the folder? ')

imageDownloader(searchWord, folderName)
