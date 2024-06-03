def calculate_total_pages(pages):

    total_pages = 0
    total_blank_sheets = 0
    for p in pages:
        if p % 2 == 1:
            total_pages += 1
        else:
            total_blank_sheets +=p
    
    total_blank_sheets = total_blank_sheets // 2
    total_pages = total_pages + total_blank_sheets
        
    return total_pages


chapter = int(input("Enter the amount of chapters:").strip())

pages = list(map(int, input().strip().split()))

print(pages)

if len(pages) != chapter:
    print("The total pages conflict with chapter count")

else:
    print("Total Sheets:",calculate_total_pages(pages))