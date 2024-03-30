#include <iostream>
#include <cstring>
#include <queue>
using namespace std;

const int N = 5e4 + 10, M = 1e6 + 7, X = 1e9 + 1;
int n, m;
struct node {
    int x, y, r;
}b[N];
typedef long long ll;
ll h[M]; // ��ϣ����
bool st[N]; // �ж��Ƿ���ʹ�
int id[M], res; // id����Ϊ��ϣ������key��Ӧ�ĵ����±�

ll get_hs(int x, int y) { // �õ�ÿ������Ĺ�ϣֵ
    return (ll)x * X + y;
}
 
int find(int x, int y) { // �ҵ������걻��ϣ����洢���±�key
    ll hs = get_hs(x, y);
    int key = (hs % M + M) % M; // ӳ�䵽��ϣ�����ڲ�
    // �����λ���Ѿ���ռ�ò��Ҳ���������Ҫ��Ĺ�ϣֵ��Ҫ��֮���ҵ���Ӧλ��
    while(h[key] != -1 && h[key] != hs) { 
    
        key++;
        if(key == M) key = 0; // ��ϣ���ߵ�ĩβ���ִ�0��ʼ
    }
    return key;
}

// �ж�x1��y1ΪԲ�ģ��뾶Ϊr��Բ�Ƿ����x��y
bool check(int x1, int y1, int r, int x, int y) { 
    int d = (x1 - x) * (x1 - x) + (y1 - y) * (y1 - y);
    return d <= r * r;
}

void bfs(int pos) {
    queue<int> q;
    q.push(pos);
    st[pos] = 1;
    while(q.size()) {
        int t = q.front();
        q.pop();
        int x = b[t].x, y = b[t].y, r = b[t].r;
        for(int xx = x - r; xx <= x + r; xx++) { // ��(x-r, y-r)ö�ٵ�(x+r, y+r)
            for(int yy = y - r; yy <= y + r; yy++) {
                int key = find(xx, yy); // �ҵ���������Ӧ�Ĺ�ϣ�±�
                // �õ��ǲ��ǵ��ף���û�б����ʹ����ܲ���ը�� 
                if(id[key] && !st[id[key]] && check(x, y, r, xx, yy)) { 
                    int pos = id[key]; // ��ö�Ӧ���ױ��
                    st[pos] = 1;
                    q.push(pos);
                }
            }
        }
    }
}

int main() {
    cin >> n >> m;
    memset(h, -1, sizeof(h));
    int x, y, r;
    for(int i = 1; i <= n; i++) { // ������ף������ϣ��
        cin >> x >> y >> r;
        b[i] = {x, y, r};
        int key = find(x, y);// �ҵ���������Ӧ�Ĺ�ϣ�±�
        if(h[key] == -1) h[key] = get_hs(x, y); // �����ϣ��Ӧλ��Ϊ�գ������
        
        // id����û�б���ǻ����ҵ���ͬһ����������뾶�ĵ���
        if(!id[key] || b[id[key]].r < r) { 
            id[key] = i;
        }
    }
    for(int i = 1; i <= m; i++) { // ö�ٵ���
        cin >> x >> y >> r;
        for(int xx = x - r; xx <= x + r; xx++) {
            for(int yy = y - r; yy <= y + r; yy++) {
                int key = find(xx, yy);
                
                // ����õ��е��ף�û�б����ʹ����ܱ�ը��
                if(id[key] && !st[id[key]] && check(x, y, r, xx, yy)) bfs(id[key]);
            }
        }
    }
    // ����ÿ�����ף����Ƿ񱻱��
    for(int i = 1; i <= n; i++) {
        int key = find(b[i].x, b[i].y); // ���������Ӧ��ϣ�±�
        int pos = id[key]; // ��ϣ�±��Ӧ�ĵ��ױ��
        if(pos && st[pos]) res++; // ����е��ײ��ұ����ʹ�
    }
    cout << res;
    return 0;
}

