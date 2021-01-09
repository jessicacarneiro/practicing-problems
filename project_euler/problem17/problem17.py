nums = ["one","two","three","four","five","six","seven","eight","nine",
        "ten"]

dec = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen",
        "eighteen","nineteen"]

tys = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

hundred = ["hundred"]

thousand = ["thousand"]

total_letters = 0

# 1..10
for n in nums:
        print(n)
        total_letters += len(n)

# 11..19
for d in dec:
        print(d)
        total_letters += len(d)

# 20..99
for i in range(0, len(tys)):
        print(tys[i])
        total_letters += len(tys[i])

        for j in range(0, len(nums) - 1):
                print(tys[i] + " " + nums[j])
                total_letters += (len(tys[i]) + len(nums[j]))

# 100...999
for i in range(0, len(nums) - 1):

        # 100,200,300,400,500,600,700,800,900
        print(nums[i] + " " + hundred[0])
        total_letters += (len(nums[i]) + len(hundred[0]))

        #101..110,..,901..910
        for j in range(0, len(nums)):
                print(nums[i] + " " + hundred[0] + " and " + nums[j])
                total_letters += (len(nums[i]) + len(hundred[0]) + len("and") + len(nums[j]))

        # 111..119,..,911..919
        for k in range(0, len(dec)):
                print(nums[i] + " " + hundred[0] + " and " + dec[k])
                total_letters += (len(nums[i]) + len(hundred[0]) + len("and") + len(dec[k]))

        # 120..199,..,920..999
        for m in range(0, len(tys)):
                print(nums[i] + " " + hundred[0] + " and " + tys[m])
                total_letters += (len(nums[i]) + len(hundred[0]) + len("and") + len(tys[m]))

                for n in range(0, len(nums) - 1):
                        print(nums[i] + " " + hundred[0] + " and " + tys[m] + "-" + nums[n])
                        total_letters += (len(nums[i]) + len(hundred[0]) + len("and") + len(tys[m]) + len(nums[n]))


print(nums[0] + " " + thousand[0])
total_letters += (len(nums[0]) + len(thousand[0]))

print("total: {}".format(total_letters))