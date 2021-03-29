# -*- encoding:utf-8-*-
import random
import argparse
import unicodedata

def fill_str(input_s="", max_size=50, fill_char=" "):
    # https://frhyme.github.io/python-libs/print_kor_and_en_full_half_width/
    l = 0
    for c in input_s:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l+=2
        else:
            l+=1
    return input_s+fill_char*(max_size-l)


class CVLabCleaningAssignment:
    def __init__(self):
        self.students = self._init_students()
        self.regions = self._init_regions()

    def _init_students(self):
        students = []
        with open ('seats.csv') as f:
            for sector in f:
                sector = sector.strip().split(',')
                if len(sector) > 3:  # few-student sector is ignored
                    students.append(sector)
        return students

    def _init_regions(self):
        regions = dict()
        regions["공용 공간 바닥, 공용 공간 책상, 소파 밑 먼지"] = 3
        regions["왼쪽 입구쪽 복도, 신발장, 옷장"] = 2
        regions["오른쪽 입구쪽 복도, 신발장, 옷장"] = 2
        regions["냉장고 정리 (유통기한 지난 것들, 이름 없는 것들)"] = 2
        regions["전자레인지 닦기, 소파 먼지 털고 오기"] = 2
        regions["대청소 이후 청소기 잔여물 제거/냉장고 옆 박스 정리"] = 2
        regions["파쇄기 비우기/복합기 옆 종이 버리기"] = 2
        return regions

    def assign(self):
        random.shuffle(self.students)  # shuffle sector
        for region, students_subset in zip(self.regions, self.students):
            random.shuffle(students_subset)  # shuffle priority
            num = self.regions[region]
            print(f'{fill_str(region)} | {students_subset[:num]}')  # slice students
        print(f'{fill_str("커피머신 청소")} | {["민교"]}')  # hardcoded assignment
        print(f'{fill_str("본인 섹터 청소, 개인 공간 청소, 개인 휴지통 비우기")} | {"나머지"}')  # hardcoded assignment


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-date', type=int, help='Random seed in a form of YYYYMM', default=202103)
    args = parser.parse_args()
    random.seed(args.date)

    print(f"\n{args.date} 차 공용 구역 청소 당번입니다.\n")
    CVLabCleaningAssignment().assign()
