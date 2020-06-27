from django.shortcuts import render

# Create your views here.
def index(request):

    myword=request.GET.get('myword')
    
    #print
    print(myword)
    
    #length
    context = dict()
    word_len=len(myword)
    context['display_len']=word_len
    
    #word count
    word_list=myword.split(" ")   #하나 하나 둘 셋 넷
    print("*****", word_list)
    
    count_dict={}
    for i in word_list:
        if i in count_dict:
            count_dict[i]+=1
        else:
            count_dict[i]=1
            
    context['display_cnt']=count_dict
    
    return render(request, 'index.html',context)