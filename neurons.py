import shoes
#https://api.mlab.com/api/1/databases/shopeiro/collections/tools?l=12&q={%22typePrefix%22:%22%D0%A2%D1%83%D1%84%D0%BB%D0%B8%22}&apiKey=gyxt40ZuBvX0-Zs_ASfIphz87os52wgf
#https://api.mlab.com/api/1/databases/shopeiro/collections/tools?l=40&q={%22typePrefix%22:%22%D0%A2%D1%83%D1%84%D0%BB%D0%B8%22,%22%D0%BF%D0%BE%D0%BB%22%20:%20%22%D0%9C%D1%83%D0%B6%D1%81%D0%BA%D0%BE%D0%B9%22}&apiKey=gyxt40ZuBvX0-Zs_ASfIphz87os52wgf
class Alts:
    def __init__(self,item_index):
        self.sample=shoes.coll_condenced[item_index]
        self.nodes = shoes.coll_condenced
        self.weights=[0.05,.2,1.1] #size,price,icolor
        self.dst=self.distances()
        self.ranked_items=[]
        for i in range(len(self.nodes)):
            self.ranked_items.append({'id':i,'dst':self.dst[i]})
        del self.ranked_items[item_index]
        self.sort_distances()


    def distances(self):
        result=[]
        for i in self.nodes:
            summ=0
            index=0
            for j in self.sample.keys():
                summ+=(i[j]-self.sample[j])**2*self.weights[index]
                index+=1
            result.append(summ)
        return result

    def sort_distances(self):
        need_sort=True
        while need_sort:
            need_sort=False
            for i in range(len(self.ranked_items)-1):
                if self.ranked_items[i]['dst']>self.ranked_items[i+1]['dst']:
                    need_sort=True
                    self.ranked_items[i],self.ranked_items[i+1]=self.ranked_items[i+1],self.ranked_items[i]


if __name__ == "__main__":
    ranked_items=[]
    a=Alts(3)
    print(a.ranked_items)
    # for i in range(len(shoes.imgs)):
    #     ranked_items.append({'img':shoes.imgs[i],'dist':d[i]})



# def generate_pickers():
#     html='<select class="image-picker show-labels show-html">'
#     for i in range(len(shoes.imgs)):
#         html+='<option data-img-src="static/thumbnails/' + shoes.imgs[i]\
#               +'" value="' +str(i)+'">'+shoes.coll[i]['description'][:18]+'</option>'
#     html+='</select>'
#     return html

# [{"type": 3, "size": 9},
#                       {"type": 2, "size": 7},
#                       {"type": 7, "size": 4},
#                       {"type": 8, "size": 5},
#                       ]