from django.shortcuts import render, redirect
from django.views import View
from .models import MonthContact, ChannelSuccess, DaySuccess, MonthSuccess
from .models import ChannelContact, FavoriteBenefit, FavoriteProduct, Favorite_Product_Benefit
from .models import AgentTotal,DayContact, SupBenefit, SupProduct, Sup_Product_Benefit
from .models import Channel
from apps.contract.models import ContractInformation
from .models import NewAgent, LocationContact, MainBenefit, MainProduct, Main_Product_Benefit
import numpy as np
from apps.contract.models import Collaborators
import json
from .ultils import *
from apps.contract.models import LifeContract
class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard/index.html')


class LifecontractView(View):
    def get(self, request):
        # list_contact = DayContact.objects.all()
        # count_list_contact = list_contact.count()
        # list_contact = list_contact[count_list_contact - 96:]
        # # lis1 = list_contact.values_list('number_customer', flat=True)
        # # a = np.array(lis1)
        # c=[]
        # b =0
        # for i in list_contact:
        #     sub_item = {}
        #     b = b + i.number_customer
        #     sub_item['snbc'] = b
        #     sub_item['nbc'] = i.number_customer
        #     sub_item['day'] = i.get_dd_mm_yyyy
        #     sub_item['hh'] = i.get_hour_minute
        #     c.append(sub_item)
        # # list_data = zip(list_contact, a, c)
        # context = {
        #     'list_data': c

        # }
        a = LifeContract()
        context = {'lc': a}
        return render(request, 'dashboard/duyet_chuyenhd/lifecontract.html', context)

   
            


class NonLifecontractView(View):
    def get(self, request):
        # list_contact = MonthContact.objects.all()
        # count_list_contact = list_contact.count()
        # list_contact = list_contact[count_list_contact - 24:]
        # last_year = list_contact[:12]
        # list_current_year = list_contact[12:]
        # list_data = zip(last_year, list_current_year)

        # context = {
        #     'list_data': list_data,
        #     'year': list_current_year[0].get_year

        # }
        return render(request, 'dashboard/duyet_chuyenhd/nonlifecontract.html')


class AddLifecontractView(View):
    def get(self, request):
        return render(request, 'dashboard/duyet_chuyenhd/addlifecontract.html')


class AddLifenoncontractView(View):
    def get(self, request):
        # list_customer = LocationContact.objects.all()
        # count_list_contact = list_customer.count()
        # list_customer = list_customer[count_list_contact - 63:]
        # name_province = list_customer.values_list('location__name_province', flat=True)
        # lis1 = list_customer.values_list('number_customer', flat=True)
        # a = np.array(lis1)
        # total_array = np.full(lis1.count(), sum(lis1))
        # weight = np.round(((lis1 / total_array) * 100), 2)
        # list_data = zip(list(name_province), a, weight)

        # context = {
        #     'list_data': list_data

        # }
        return render(request, 'dashboard/duyet_chuyenhd/addnonlifecontract.html')


class CustomerView(View):
    def get(self, request):

        return render(request, 'dashboard/duyet_chuyenhd/customer.html')


class PersonalinformationView(View):
    def get(self, request):
        # list_customer = DaySuccess.objects.all()
        # count_list_customer = list_customer.count()
        # last_month = list_customer[count_list_customer - 30:]
        # last_m_1 = last_month.values_list('number_customer', flat=True)
        # last_m_1_array = np.array(last_m_1)
        # sum_last_m_1 = sum(last_m_1_array)
        # last_m_2 = last_month.values_list('number_policy', flat=True)
        # last_m_2_array = np.array(last_m_2)
        # sum_last_m_2 = sum(last_m_2_array)
        # ratio_30 = np.round((sum_last_m_2/sum_last_m_1)*100,2)
        # list_data_30 = [sum_last_m_1, sum_last_m_2, ratio_30]
        # last_week = list_customer[count_list_customer - 7:]
        # last_w_1 = last_week.values_list('number_customer', flat=True)
        # last_w_1_array = np.array(last_w_1)
        # sum_last_w_1 = sum(last_w_1_array)
        # last_w_2 = last_week.values_list('number_policy', flat=True)
        # last_w_2_array = np.array(last_w_2)
        # sum_last_w_2 = sum(last_w_2_array)
        # ratio_7 = np.round((sum_last_w_2 / sum_last_w_1)*100,2)
        # list_data_7 = [sum_last_w_1, sum_last_w_2, ratio_7]
        # last_tree_day = list_customer[count_list_customer - 3:]
        # last_tree_1 = last_tree_day.values_list('number_customer', flat=True)
        # last_tree_1_array = np.array(last_tree_1)
        # sum_last_tree_1 = sum(last_tree_1_array)
        # last_tree_2 = last_tree_day.values_list('number_policy', flat=True)
        # last_tree_2_array = np.array(last_tree_2)
        # sum_last_tree_2 = sum(last_tree_2_array)
        # ratio_3 = np.round((sum_last_tree_2 / sum_last_tree_1)*100,2)
        # list_data_3 = [sum_last_tree_1, sum_last_tree_2, ratio_3]
        # last_one_day = list_customer[count_list_customer - 1:]
        # last_one_1 = last_one_day.values_list('number_customer', flat=True)
        # last_one_1_array = np.array(last_one_1)
        # sum_last_one_1 = sum(last_one_1_array)
        # last_one_2 = last_one_day.values_list('number_policy', flat=True)
        # last_one_2_array = np.array(last_one_2)
        # sum_last_one_2 = sum(last_one_2_array)
        # ratio_1 = np.round((sum_last_one_2/sum_last_one_1)*100,2)
        # list_data_1 = [sum_last_one_1, sum_last_one_2, ratio_1]
        # context = {
        #     'list_data_30': list_data_30,
        #     'list_data_7': list_data_7,
        #     'list_data_3': list_data_3,
        #     'list_data_1': list_data_1,
        # }
        return render(request, 'dashboard/profile/personalinformation.html')



class ChangepasswordView(View):
    def get(self, request):
        # list_customer = MonthSuccess.objects.all()
        # count_list_customer = list_customer.count()
        # last_list = list_customer[count_list_customer - 12:]
        # last_customer = last_list.values_list('number_customer', flat=True)
        # last_customer_array = np.array(last_customer)
        # last_policy = last_list.values_list('number_policy', flat=True)
        # last_policy_array = np.array(last_policy)
        # ratio = np.round((last_policy_array/last_customer_array)*100,2)
        # list_data = zip(last_customer_array, last_policy_array, ratio)

        # context = {
        #     'list_data': list_data

        # }
        return render(request, 'dashboard/profile/changepassword.html')



class SystemlogView(View):
    def get(self, request):
        # yyyy = get_year()
        # print_array = []

        # for i in range(1, 13):
        #     sub_item = {}
        #     sub_item['m'] = i
        #     sub_data = number_customer_to_m(i, yyyy)
            
        #     sub_item['data'] = sub_data
        #     print_array.append(sub_item)
        #     last_data = get_line_chart_print_value()
        # context = {
        #     'list_data': print_array,
        #     'last_data': last_data

        # }
        return render(request, 'dashboard/profile/system_log.html')


class AgenttotalView(View):
    def get(self, request):
            list_agent = AgentTotal.objects.all()
            count_list_agent = list_agent.count()
            list_agent = list_agent[count_list_agent - 24:]
            last_year = list_agent[:12]
            list_current_year = list_agent[12:].values_list()

            #ratio = list_current_year.number_agent/last_year.number_agent
            lis1 = last_year.values_list('number_agent', flat=True)
            lis2 = list_current_year.values_list('number_agent', flat=True)
            li1 = [i for i in lis1]
            li2 = [i for i in lis2]
            a = np.array(li1)
            b = np.array(li2)
            ratio = np.round((a/b)*100,2)
            list_data = zip(lis1, lis2, ratio)
            diagram1 = json.dumps(li1)
            diagram2 = json.dumps(li2)
            context = {
                'list_data': list_data,
                'diagram1': diagram1,
                'diagram2': diagram2
            }
            return render(request, 'dashboard/agent_statistics/agent_total.html', context)


class NewagentView(View):
    def get(self, request):
        list_agent = NewAgent.objects.all()
        count_list_agent = list_agent.count()
        list_agent = list_agent[count_list_agent - 24:]
        last_year = list_agent[:12]
        list_current_year = list_agent[12:].values_list()

        # ratio = list_current_year.number_agent/last_year.number_agent
        lis1 = last_year.values_list('number_agent', flat=True)
        lis2 = list_current_year.values_list('number_agent', flat=True)
        li1 = [i for i in lis1]
        li2 = [i for i in lis2]
        a = np.array(li1)
        b = np.array(li2)
        ratio = np.round((a/b)*100,2)
        list_data = zip(lis1, lis2, ratio)
        diagram1 = json.dumps(li1)
        diagram2 = json.dumps(li2)
        context = {
            'list_data': list_data,
            'diagram1': diagram1,
            'diagram2': diagram2
        }
        return render(request, 'dashboard/agent_statistics/new_agent.html', context)


class AgentchannelView(View):
    def get(self, request):
        yyyy = get_year()
        print_array = []
        last_zip_object = []

        for i in range(1, 13):
            sub_item = {}
            sub_item['m'] = i
            sub_data = sum_agency_to_m(i, yyyy)
            sub_item['data'] = sub_data
            print_array.append(sub_item)
            h = [list(a) for a in sum_agency_to_m(i, yyyy)]
            if len(h) > 0:
                last_zip_object = h

        last_zip_object = np.array(last_zip_object)
        split = np.hsplit(last_zip_object, 3)
        ga = split[2].astype(float)
        last_list_data = np.around(ga, 0)
        context = {
            'list_data': print_array,
            'last_list_data': last_list_data
        }
        return render(request, 'dashboard/agent_statistics/agent_channel.html', context)


class MainproductView(View):
    def get(self, request):
        list_sp = [

        ]

        products = MainProduct.objects.all()
        sum_like = sum(products.values_list('number_customer', flat=True))
        for item in products:
            subitem = {}
            subitem['name_product'] = item.name_product
            subitem['like'] = item.number_customer
            subitem['benefit'] = Main_Product_Benefit.objects.filter(
                product_id=item.id).values_list('benefit__name_benefit', flat=True)
            subitem['time'] = item.created_time
            subitem['tytrong'] = np.round(item.number_customer/sum_like*100,2)

            list_sp.append(subitem)


        context = {
            'list_sp': list_sp

        }
        return render(request, 'dashboard/product_statistics/main_product.html', context)


class SupproductView(View):
    def get(self, request):
        list_sp = [

        ]

        products = SupProduct.objects.all()
        sum_like = sum(products.values_list('number_customer', flat=True))
        for item in products:
            subitem = {}
            subitem['name_product'] = item.name_product
            subitem['like'] = item.number_customer
            subitem['benefit'] = Sup_Product_Benefit.objects.filter(
                product_id=item.id).values_list('benefit__name_benefit', flat=True)
            subitem['time'] = item.created_time
            subitem['tytrong'] = np.round(item.number_customer / sum_like * 100, 2)

            list_sp.append(subitem)

        context = {
            'list_sp': list_sp

        }
        return render(request, 'dashboard/product_statistics/sup_product.html', context)


class FavoriteproductView(View):
    def get(self, request):
        list_sp = [

        ]

        products = FavoriteProduct.objects.all()
        for item in products:
            subitem = {}
            subitem['time'] = item.created_time
            subitem['name_product'] = item.name_product
            subitem['sa'] = item.sa
            subitem['policy_term'] = item.policy_term
            subitem['payment_term'] = item.payment_term
            subitem['ways_to_get_benefit'] = item.ways_to_get_benefit
            subitem['benefit'] = Favorite_Product_Benefit.objects.filter(
                product_id=item.id).values_list('benefit__name_benefit', flat=True)
            list_sp.append(subitem)

        context = {
            'list_sp': list_sp

        }
        return render(request, 'dashboard/product_statistics/favorite_product.html', context)


class CalendarView(View):
    def get(self, request):
        return render(request, 'dashboard/calendar/calendar.html')


class InboxView(View):
    def get(self, request):
        return render(request, 'dashboard/mailbox/inbox.html')


class ComposeView(View):
    def get(self, request):
        return render(request, 'dashboard/mailbox/compose.html')


class ReadView(View):
    def get(self, request):
        return render(request, 'dashboard/mailbox/read.html')


class UseragentView(View):
    def get(self, request):
        return render(request, 'dashboard/user_agent/user.html')


class SearchagentView(View):
    def get(self, request):
        return render(request, 'dashboard/search_agent/search.html')


class TrangThaiNhanTho(View):
    def get(self, request):
        return render(request, 'dashboard/tinh_trang/nhantho.html')


class TrangThaiPhiNhanTho(View):
    def get(self, request):
        return render(request, 'dashboard/tinh_trang/phinhantho.html')

    
class StatusTrangThaiNhanTho(View):
    def get(self, request):
        return render(request, 'dashboard/tinh_trang/statusnhantho.html')


class StatusTrangThaiPhiNhanTho(View):
    def get(self, request):
        return render(request, 'dashboard/tinh_trang/statusphinhantho.html')


class AddTrangThaiNhanTho(View):
    def get(self, request):
        return render(request, 'dashboard/add_baohiem/addnhantho.html')

    def post(self, request):
        buyer = request.POST.get("buyer")
        buyer_sex = request.POST.get("buyer_sex")
        buyer_cmnd = request.POST.get("buyer_cmnd")
        buyer_image = request.POST.get("buyer_image")
        buyer_birth = request.POST.get("buyer_birth")
        buyer_phone = request.POST.get("buyer_phone")
        buyer_email = request.POST.get("buyer_email")
        receiver = request.POST.get("receiver")
        receiver_cmnd = request.POST.get("receiver_cmnd")
        receiver_image = request.POST.get("receiver_image")
        receiver_birth = request.POST.get("receiver_birth")
        receiver_sex = request.POST.get("receiver_sex")
        beneficiary = request.POST.get("beneficiary")
        beneficiary_cmnd = request.POST.get("beneficiary_cmnd")
        beneficiary_relationship = request.POST.get("beneficiary_relationship")
        beneficiary_image = request.POST.get("beneficiary_image")
        beneficiary_birth = request.POST.get("beneficiary_birth")
        beneficiary_sex = request.POST.get("beneficiary_sex")
        presenter_name = request.POST.get("presenter_name")
        presenter_id = request.POST.get("presenter_id")
        product_name = request.POST.get("product_name")
        product_company = request.POST.get("product_company")
        product_phi = request.POST.get("product_phi")
        product_year_contract = request.POST.get("product_year_contract")
        product_year_phi = request.POST.get("product_year_phi")
        product_frequency_phi = request.POST.get("product_frequency_phi")
        product_insurance_money = request.POST.get("product_insurance_money")
        supplementary_product_name = request.POST.get("supplementary_product_name")
        supplementary_product_company = request.POST.get("supplementary_product_company")
        supplementary_product_phi = request.POST.get("supplementary_product_phi")
        supplementary_product_year_contract = request.POST.get("supplementary_product_year_contract")
        supplementary_product_year_phi = request.POST.get("supplementary_product_year_phi")
        supplementary_product_frequency_phi = request.POST.get("supplementary_product_frequency_phi")
        supplementary_product_insurance_money = request.POST.get("supplementary_product_insurance_money")
        pay_main_product = request.POST.get("pay_main_product")
        pay_phu_product = request.POST.get("pay_phu_product")
        pay_total_phi = request.POST.get("pay_total_phi")
        pay_tax = request.POST.get("pay_tax")
        total_payment_amount = request.POST.get("total_payment_amount")
        information_received = request.POST.get("information_received")
        information_received_name = request.POST.get("information_received_name")
        information_received_email = request.POST.get("information_received_email")
        information_received_phone = request.POST.get("information_received_phone")
        information_received_address = request.POST.get("information_received_address")
        ContractInformation.objects.create(buyer=buyer,buyer_sex=buyer_sex,buyer_cmnd=buyer_cmnd,buyer_image=buyer_image,
        buyer_birth=buyer_birth,buyer_phone=buyer_phone,buyer_email=buyer_email,receiver=receiver,
        receiver_cmnd=receiver_cmnd,receiver_image=receiver_image,receiver_birth=receiver_birth,
        receiver_sex=receiver_sex,beneficiary=beneficiary,beneficiary_cmnd=beneficiary_cmnd,beneficiary_relationship=beneficiary_relationship,
        beneficiary_image=beneficiary_image,beneficiary_birth=beneficiary_birth,beneficiary_sex=beneficiary_sex,
        presenter_name=presenter_name,presenter_id=presenter_id,product_name=product_name,product_company=product_company,
        product_phi=product_phi,product_year_contract=product_year_contract,product_year_phi=product_year_phi,product_frequency_phi=product_frequency_phi,
        product_insurance_money=product_insurance_money,supplementary_product_name=supplementary_product_name,supplementary_product_company=supplementary_product_company,
        supplementary_product_phi=supplementary_product_phi,supplementary_product_year_contract=supplementary_product_year_contract,supplementary_product_year_phi=supplementary_product_year_phi,
        supplementary_product_frequency_phi=supplementary_product_frequency_phi,supplementary_product_insurance_money=supplementary_product_insurance_money,
        pay_main_product=pay_main_product,pay_phu_product=pay_phu_product,pay_total_phi=pay_total_phi,pay_tax=pay_tax,total_payment_amount=total_payment_amount,
        information_received=information_received,information_received_name=information_received_name,information_received_email=information_received_email,
        information_received_phone=information_received_phone,information_received_address=information_received_address
        )
       
        return render(request, 'dashboard/add_baohiem/addnhantho.html')    


class AddTrangThaiPhiNhanTho(View):
    def get(self, request):
        return render(request, 'dashboard/add_baohiem/addphinhantho.html')


class HdMoi(View):
    def get(self, request):
        return render(request, 'dashboard/ql_hopdong/hd_moi.html')


class LichSuHopDong(View):
    def get(self, request):
        return render(request, 'dashboard/ql_hopdong/ls_hopdong.html')
        

class DuyetCay(View):
    def get(self, request):
        return render(request, 'dashboard/ql_ctv/lifecontract.html')


class GanNhomKinhDoanh(View):
    def get(self, request):
        return render(request, 'dashboard/gan-nhom-kd/gan_kd.html')


class CayGanNhomKinhDoanh(View):
    def get(self, request):
        return render(request, 'dashboard/gan-nhom-kd/cay-gan-nhom.html')


class TaiKhoan(View):
    def get(self, request):
        data=Collaborators.objects.all()[:5]
        print(data)
        context={
            "listdata" : data
        }
        return render(request, 'dashboard/ql_ctv/taikhoan.html',context)



class ChinhSach(View):
    def get(self, request):
        return render(request, 'dashboard/customer_contact/location_contact.html')


class thongbao(View):
    def get(self, request):
        return render(request, 'dashboard/customer_contact/month_contact.html')


class DaycontactView(View):
    def get(self, request):
        return render(request, 'dashboard/customer_contact/day_contact.html')


class ChannelcontactView(View):
    def get(self, request):
        return render(request, 'dashboard/customer_contact/channel_contact.html')


class TaiLieu(View):
    def get(self, request):
        return render(request, 'dashboard/thu_vien/tailieu.html')


class TongQuanHopDong(View):
    def get(self, request):
        return render(request, 'dashboard/baocao/tongquan.html')


class TongQuanCtv(View):
    def get(self, request):
        return render(request, 'dashboard/baocao/tongquanctv.html')


class KPY(View):
    def get(self, request):
        return render(request, 'dashboard/baocao/kpy.html')


class StatusTongQuanHopDong(View):
    def get(self, request):
        return render(request, 'dashboard/baocao/statushd.html')


class StatusTongQuanCtv(View):
    def get(self, request):
        return render(request, 'dashboard/baocao/statusctv.html')


class StatusKPY(View):
    def get(self, request):
        return render(request, 'dashboard/baocao/statuskpy.html')


class AddLifecontractView(View):
    def get(self, request):
        return render(request, 'dashboard/duyet_chuyenhd/addlifecontract.html')


class StatusDuyetCay(View):
    def get(self, request):
        return render(request, 'dashboard/ql_ctv/addlifecontract.html')

        