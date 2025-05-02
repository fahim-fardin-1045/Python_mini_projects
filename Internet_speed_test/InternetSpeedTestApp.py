import speedtest

st = speedtest.Speedtest() 
download = st.download()
upload = st.upload()

download = download/1000000
upload = upload/1000000

print("Your ⏬ Download speed is", round(download, 3), 'Mbps')
print("Your ⏫ Upload speed is", round(upload, 3), 'Mbps')

st.get_servers([])
ping = st.results.ping

print("Your Ping is", ping)